import requests
from bs4 import BeautifulSoup
header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
'x-requested-with': 'XMLHttpRequest',
'content-type': 'application/json'
}
#html = requests.get('https://www.vivino.com/wineries/monterebro/wines/monterebro-rosado-nv',headers=header)
html = requests.get('https://www.vivino.com/wineries/colgin-cellars/wines/colgin-cellars-ix-estate-red-2012',headers=header)
bs4 = BeautifulSoup(html.text,'lxml')
#print(bs4.prettify())
winery = bs4.find('a',class_='wine-page__header__information__details__name__winery').get_text().strip()
name = bs4.find('span',class_='wine-page__header__information__details__name__vintage').get_text().strip()

region = bs4.find('a',class_='wine-page__header__information__details__location__region').get_text().strip()
country = bs4.find("a",class_='wine-page__header__information__details__location__country').get_text().strip()

averLabel = bs4.find('div',class_='wine-page__header__information__details__average-rating__label').get_text().strip()
averValue = bs4.find('div',class_='wine-page__header__information__details__average-rating__value__number').get_text().strip()

divs = bs4.find_all('div',class_='wine-page__summary__item')
summary = ""
for div in divs:

    summaryHeader = div.find('div',class_='wine-page__summary__item__header').get_text().strip()
    summary += summaryHeader+":"
    for a in div.find_all('a'):
        summary +=a.get_text().strip()+','
    summary = summary[:-1]+'\n'


print(winery)
print(name)
print(region,country)
print(averLabel,averValue)
print(summary)