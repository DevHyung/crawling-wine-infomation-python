import requests
import time
import json
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
'x-requested-with': 'XMLHttpRequest',
'content-type': 'application/json'
}
urlFormat = 'https://www.vivino.com/wineries/{}/wines/{}'
total = 737780
pageLimit = int(total / 25)+1 # 29512
url = 'https://www.vivino.com/api/explore/explore?country_code=kr&currency_code=KRW&grape_filter=varietal&merchant_id=&min_rating=1&order_by=&order=desc&page={}&price_range_max=500000&price_range_min=0&wine_type_ids[]=1&wine_type_ids[]=2&wine_type_ids[]=3&wine_type_ids[]=4&wine_type_ids[]=7&wine_type_ids[]=24'
#===
START = 1
END = 100
while True:
    print("{} ~ {} 까지 파싱시작".format(START,END))
    f = open('미완/{}~{}.txt'.format(START,END),'w')
    for i in range(START,END):
        print("\t>>> ",i," page...")
        html = requests.get(url.format(i),headers=header)
        jsonStr = json.loads(html.text)
        for matche in jsonStr['explore_vintage']['matches']:
            try:
                name = matche['vintage']['seo_name']
                winery = matche['vintage']['wine']['winery']['seo_name']
                #print(urlFormat.format(winery,name))
                f.write(urlFormat.format(winery,name)+'\n')
            except:
                #print('없음::','https://www.vivino.com/wines/'+name)
                f.write('https://www.vivino.com/wines/'+name+ '\n')
    f.close()

    START = END
    END += 100
    if END > 737780 and END == 737880 + 1:
        break
    elif END > 737780:
        END = 737780 + 1
