#개드립넷 인기글 크롤링

#import requests
import urllib.request
from bs4 import BeautifulSoup

# 1) reqeusts 라이브러리를 활용한 HTML 페이지 요청
# 1-1) res 객체에 HTML 데이터가 저장되고, res.content로 데이터를 추출할 수 있음
#res = requests.get('https://www.dogdrip.net/?mid=dogdrip&sort_index=popular')
url = 'https://www.dogdrip.net/?mid=dogdrip&sort_index=popular'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
# 2) HTML 페이지 파싱 BeautifulSoup(HTML데이터, 파싱방법)
# 2-1) BeautifulSoup 파싱방법
# 2-2) HTML코드를 soup이라는 python객체로 변환, (변환할 코드, 파싱할 파서)
soup = BeautifulSoup(html, 'html.parser')

# 3) 필요한 데이터 검색, title이라는 python객체로 변환
title = soup.select('td.title > a')
# 4) 필요한 데이터 추출

for i in title:
    print(i.text)
    print(i.attrs['href'])
# #     print(i.attrs['title'])
#     print(i.attrs['a.href'])
#     print()
#main > div > div.eq.section.secontent.background-color-content > div > div.ed.board-list > table > tbody > tr:nth-child(1) > td.title > a
