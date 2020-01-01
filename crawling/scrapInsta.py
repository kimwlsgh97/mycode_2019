from selenium import webdriver
from urllib.parse import quote_plus

baseURL = "https://www.instagram.com/explore/tags/"
plusURL = input("검색할 태그를 입력하세요 : ")
URL = baseURL + quote_plus(plusURL)

driver = webdriver.Chrome()
driver.get(URL)
content = driver.find_element_by_class_name('div.v1Nh3')
print(content)
driver.close()
