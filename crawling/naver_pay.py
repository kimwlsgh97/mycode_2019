from selenium import webdriver
from bs4 import BeautifulSoup
import time
#네이버 로그인
URL = "https://nid.naver.com/nidlogin.login?"

driver = webdriver.Chrome()
driver.get(URL)
id = 'kimwlsgh97'
pw = 'KJHwhsgh1!'
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
time.sleep(3)

#네이버 페이
driver.get('https://order.pay.naver.com/home')
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.select('div.good_info > a > p')

for n in notices:
    print(n.text.strip())
