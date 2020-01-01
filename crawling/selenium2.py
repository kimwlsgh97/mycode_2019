#google login
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

URL = "https://accounts.google.com/signin/v2/identifier?service=youtube&uilel=3&passive=true&continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Dko%26next%3D%252F&hl=ko&ec=65620&flowName=GlifWebSignIn&flowEntry=ServiceLogin"

driver = webdriver.Chrome('/Users/jinho/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get(URL)

#driver.execute_script("document.getElementById('fontBadaEventPopup').style.display='none';")
driver.find_element_by_name('identifier').send_keys('jinho971031')
driver.find_element_by_id('identifierNext').click()
driver.find_element_by_name('password').send_keys('KJHwhsgh9(')
# password = driver.find_element_by_id('passwordNext')
# driver.execute_script("arguments[0].click();", password)
driver.find_element_by_id('passwordNext').send_keys('\ue007') # id passwordNext를 찾아 엔터키(\ue007)을 누름
#driver.find_element_by_xpath('//div[@id="passwordNext"]').click()
#경고창 무시
#driver.switch_to_alert().dismiss()
#팝업창 무시
#Options.addArguments("==disalbe-popup-blocking")
driver.implicitly_wait(10)
#유튜브 핫 접속
#driver.get('https://www.youtube.com/feed/trending')
HOT = driver.find_element_by_id('endpoint')
driver.execute_script("arguments[0].click();", HOT)

#html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# notices = driver.find_element_by_xpath('//*[@id="video-title"]')
#
# for n in notices:
#     print(n.text)
