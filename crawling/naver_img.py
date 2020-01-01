from selenium import webdriver
from urllib.parse import quote_plus
from urllib.request import urlopen
from bs4 import BeautifulSoup

baseURL = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
plusURL = input("찾고싶은 이미지 검색 : ")
URL = baseURL + quote_plus(plusURL)

driver = webdriver.Chrome()
driver.get(URL)
req = driver.page_source
#데이터 정리를 위한 BeautifulSoup사용
soup = BeautifulSoup(req, 'html.parser')
imgs = soup.find_all('img',{'class':'_img'})

img_num = 1
for i in imgs:
    imgURL = i['src']
    if 'http' in imgURL:
        with urlopen(imgURL) as f:
            with open('./'+plusURL+'/' + plusURL + str(img_num) + '.jpg', 'wb') as h:
                some = f.read()
                h.write(some)
                img_num += 1

print(f"{img_num}개의 사진을 다운로드 받았습니다")
driver.close()
