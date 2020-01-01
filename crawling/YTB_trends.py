#google login
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

URL = "https://www.youtube.com/feed/trending"

driver = webdriver.Chrome('/Users/jinho/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get(URL)
driver.implicitly_wait(10)
html


#html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# notices = driver.find_element_by_xpath('//*[@id="video-title"]')
#
# for n in notices:
#     print(n.text)
