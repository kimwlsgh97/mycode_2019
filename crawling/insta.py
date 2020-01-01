from selenium import webdriver
import time
#네이버 로그인

def insta_login():
    driver = webdriver.Chrome()
    URL = "https://www.instagram.com/accounts/login/"
    driver.get(URL)
    time.sleep(5)
    driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input').send_keys('jinho971031')
    driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input').send_keys('KJHwhsgh9(')
    driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button').click()
    time.sleep(3)
