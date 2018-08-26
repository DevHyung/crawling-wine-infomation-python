import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook,Workbook
import os
import shutil
def save_excel(_FILENAME, _DATA, _HEADER):
    if os.path.exists(_FILENAME):
        if _DATA == None:
            return None
        book = load_workbook(_FILENAME)
        sheet = book.active
        sheet.append(_DATA)
        #for depth1List in _DATA:
            #sheet.append(depth1List)
        book.save(_FILENAME)
    else:  # 새로만드는건
        if _HEADER == None:
            print(">>> 헤더 리스트를 먼저 넣어주세요")
            return None
        book = Workbook()
        sheet = book.active
        sheet.title = '시트이름'
        sheet.append(_HEADER)
        sheet.column_dimensions['A'].width = 20
        sheet.column_dimensions['B'].width = 20
        sheet.column_dimensions['C'].width = 20
        sheet.column_dimensions['D'].width = 20
        sheet.column_dimensions['E'].width = 20
        sheet.column_dimensions['F'].width = 40
        book.save(_FILENAME)

header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
'x-requested-with': 'XMLHttpRequest',
'content-type': 'application/json'
}
'''----------------- 환경설정 부분 ---------------------'''
FILENAME = "vivino1000~.xlsx"
HEADER = ['Winery','Name', 'Region', 'Country', 'Rating', 'Summary']
# init
save_excel(FILENAME,None,HEADER)
f2 = open('error.txt','a')
'''---------------------------------------------------'''
START = 1000
END = 1100
while True:
    print(">>> {} 파일 실행중".format("./미완/{}~{}.txt".format(START,END)))
    lines = open("./미완/{}~{}.txt".format(START,END)).readlines()
    tmp = []
    idx = 1
    for url in lines:
        print("{}번째 : {} 실행중..".format(idx, url.strip()))
        idx += 1
        dataList = []
        #
        html = requests.get(url.strip(),headers=header)
        bs4 = BeautifulSoup(html.text,'lxml')
        #
        try:
            name = bs4.find('span',class_='wine-page__header__information__details__name__vintage').get_text().strip()
        except:#새로운페이지
            name = '-'
            print(">>> Move")
            f2.write(url)
            continue
        try:
            winery = bs4.find('a',class_='wine-page__header__information__details__name__winery').get_text().strip()
        except:
            winery = '-'
            print("C1",end='@')

        try:
            region = bs4.find('a',class_='wine-page__header__information__details__location__region').get_text().strip()
        except:
            region = '-'
            print("C2", end='@')
        try:
            country = bs4.find("a",class_='wine-page__header__information__details__location__country').get_text().strip()
        except:
            country = '-'
            print("C3", end='@')
        try:
            averLabel = bs4.find('div',class_='wine-page__header__information__details__average-rating__label').get_text().strip()
        except:
            averLabel = '-'
            print("C4", end='@')
        try:
            averValue = bs4.find('div',class_='wine-page__header__information__details__average-rating__value__number').get_text().strip()
        except:
            averValue = '-'
            print("C5", end='@')

        #
        divs = bs4.find_all('div',class_='wine-page__summary__item')
        summary = ""
        for div in divs:
            summaryHeader = div.find('div',class_='wine-page__summary__item__header').get_text().strip()
            summary += summaryHeader+":"
            isVoid = True
            for a in div.find_all('a'):
                summary +=a.get_text().strip()+','
                isVoid = False
            for a in div.find_all('span'):
                summary += a.get_text().strip() + ','
                isVoid = False
            if isVoid:
                summary += div.find('div',class_='wine-page__summary__item__content').get_text().strip() + ','
            summary = summary[:-1]+'\n'

        dataList.append(winery)
        dataList.append(name)
        dataList.append(region)
        dataList.append(country)
        dataList.append(averLabel+' '+averValue)
        dataList.append(summary)
        #tmp.append(dataList)
        save_excel(FILENAME,dataList,None)
    START = END
    END += 100
    if END > 737780 and END == 737880 + 1:
        break
    elif END > 737780:
        END = 737780 + 1

f2.close()