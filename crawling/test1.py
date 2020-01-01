from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.google.co.in/")
list_links=driver.find_elements_by_tag_name('a')

for i in list_links:
    print(i.get_attribute('href'))
