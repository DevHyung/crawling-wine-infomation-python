
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from openpyxl import load_workbook
from openpyxl import Workbook

#html = requests.get('https://delectable.com/wine/hamilton-russell-vineyards/hemel-en-aarde-valley-chardonnay')
#bs4 = BeautifulSoup(html.text,'lxml')
#print(bs4.prettify())
def log(tag, text):
	# Info tag
	if(tag == 'i'):
		print("[INFO] " + text)
	# Error tag
	elif(tag == 'e'):
		print("[ERROR] " + text)
	# Success tag
	elif(tag == 's'):
		print("[SUCCESS] " + text)

def save_excel(_FILENAME,_DATA,_HEADER):
    if os.path.exists(_FILENAME):
        if _DATA == None:
            return None
        book = load_workbook(_FILENAME)
        sheet = book.active
        sheet.append(_DATA)
        book.save(_FILENAME)
    else: # 새로만드는건
        book = Workbook()
        sheet = book.active
        sheet.title = '시트이름'
        sheet.append(_HEADER)
        sheet.column_dimensions['A'].width = 20
        sheet.column_dimensions['B'].width = 20
        sheet.column_dimensions['C'].width = 20
        sheet.column_dimensions['D'].width = 20
        sheet.column_dimensions['E'].width = 20
        sheet.column_dimensions['F'].width = 20
        book.save(_FILENAME)



if __name__ == "__main__":
    FILENAME = "delectable.xlsx"
    HEADER = ['와인 이름', '와이너리 이름', '생산지 정보', '품종 정보', '푸드 페어링', '평가 정보']
    save_excel(FILENAME,None,HEADER)
