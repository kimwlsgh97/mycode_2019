from selenium import webdriver

URL = "https://nid.naver.com/nidlogin.login?"

driver = webdriver.Chrome()
driver.get(URL)
search_box = driver.find_element_by_name("q")
search_box.send_keys("인스타그램")
search_box.submit()
