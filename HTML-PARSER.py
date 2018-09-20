from bs4 import BeautifulSoup


bs4 = BeautifulSoup(open('html.txt',encoding='utf8').read(),'lxml')
divs = bs4.find_all('div',class_='explorerCard__explorerCard--3Q7_0 explorerPageResults__explorerCard--3q6Qe')

print(len(divs))