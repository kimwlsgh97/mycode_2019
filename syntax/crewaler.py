# #!C:\Python27\python.exe
# #-*- coding:utf-8 -*-
# print("content-type: text/html; charset=utf-8\n")
import requests
from bs4 import BeautifulSoup


res = requests.get('https://www.dogdrip.net/?mid=dogdrip&sort_index=popular')
soup = BeautifulSoup(res.content, 'html.parser')
my_titles = soup.select('main > div > div.eq.section.secontent.background-color-content > div > div.ed.board-list > table > tbody > tr > .title > a')

for i in my_titles:
    print(i.text)
