#selenium으로 웹페이지 컨트롤 하기

#C:\Users\jinho/Downloads/chromedriver

#Selenium은 webdriver api를 통해 브라우저를 제어한다.
#webdriver import
from selenium import webdriver
#driver라는 이름의 webdriver 객체 생성
driver = webdriver.Chrome('/Users/jinho/Downloads/chromedriver')
#암묵적으로 웹의 로드를 3초 기다려주기
driver.implicitly_wait(3)
#url 접근
driver.get('https://www.youtube.com/feed/trending')
