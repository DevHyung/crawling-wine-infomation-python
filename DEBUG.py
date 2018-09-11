import time
from selenium import webdriver
from bs4 import BeautifulSoup
if __name__ == '__main__':
    SCROLL_PAUSE_TIME = 0.5
    driver = webdriver.Chrome('chromedriver')
    driver.maximize_window()
    driver.get('https://www.vivino.com/')
    gogo = input(">>> 시작할때 신호주세요 : ")
    cnt = int(input(">>> 개수를 입력하세요 :"))
    filename = input(">>> 파일이름을 써주세요 :")
    idx2 = 1
    idx = 1
    while True:
        # Scroll down to bottom
        last_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        while True:
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)
            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                idx += 1
                break
            else:
                idx = 1
                idx2 = 1
            last_height = new_height
        #
        bs4 = BeautifulSoup(driver.page_source, 'lxml')
        divs = bs4.find_all('div', class_='explorerCard__explorerCard--3Q7_0 explorerPageResults__explorerCard--3q6Qe')
        if int(len(divs)) > cnt:
            break
        #

        if idx >= 10:
            #what = input(">>> 더할껀지 1, 멈출껀지 0 ::")
            driver.execute_script("window.scrollTo(0,0);")
            print(">>> 맨위로")
            idx2 += 1
        if idx2 >= 4:
            break


    f = open(filename+'.txt',encoding='utf8')
    f.write(driver.page_source)
    f.close()

    driver.quit()