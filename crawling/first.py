#BeautifulSoup 과 urllib이라는 라이브러리를 활용한 크롤링
import urllib.request
from bs4 import BeautifulSoup

#url = 'https://search.naver.com/search.naver?sm=top_brd&fbm=1&ie=utf8&query=%ED%95%9C%EB%A1%9C+%EC%A0%88%EA%B8%B0'
base_url = 'https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query='
plus_url = input('검색어를 입력하세요 : ')
url = base_url + plus_url
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
title = soup.find_all(class_='_sp_each_title')

#ren(title)
for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()
