from selenium import webdriver
import requests
import time
from tqdm import tqdm


def pint_login(driver):   #핀터레스트 로그인
    URL = "https://www.pinterest.co.kr/"
    driver.get(URL)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div/div/div/div/div[3]/div/div[1]/div/div/div[2]/button/div').click()
    time.sleep(1)
    driver.find_element_by_name('id').send_keys('kimwlsgh97@naver.com')
    time.sleep(1)
    driver.find_element_by_name('password').send_keys('KJHwhsgh1!')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="__PWS_ROOT__"]/div/div/div/div/div[3]/div/div[1]/div/div/div[1]/div/div/div/div[3]/form/div[5]/button/div').click()
    time.sleep(3)


def page_dw(driver):    #페이지 스크롤 다운
    from selenium.webdriver.common.keys import Keys
    body = driver.find_element_by_css_selector('body')
    for i in range(0,3):
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
    time.sleep(2)


def link_cl(driver):    #이미지 링크 수집
    imgs = driver.find_elements_by_css_selector('img.hCL')
    result = []
    for img in imgs:
        if img.get_attribute('src') is not None:
            result.append(img.get_attribute('src'))
    return result



def all_of_them(driver,i,keyword):
    time.sleep(1)
    # 페이지 스크롤 다운
    page_dw(driver)
    # 이미지 url 수입
    imgs = link_cl(driver)
    # 비어있는 링크 제외
    links = []
    for img in imgs:
        if img is not None:
            links.append(img)
    import os
    # 디렉토리 생성
    if not os.path.isdir('./pint_{}{}'.format(keyword,i)):
        os.mkdir('./pint_{}{}'.format(keyword,i))

    # 다운로드 시작
    for index, link in tqdm(enumerate(links)):
        savename = f'./pint_{keyword}{i}/{keyword}_{index}.jpg'
        mem=requests.get(link).content
        with open(savename, "wb") as f:    #바이너리(이미지)일 경우 'wb',  텍스트일 경우 'w'
            f.write(mem)
        time.sleep(1)


def get_pint_img(keyword):
    # 사용자입력
    page_D = int(input("페이지 다운 횟수 : "))
    # 크롤링 웹 설정
    driver = webdriver.Chrome()
    # 핀터레스트 로그인
    pint_login(driver)
    # 핀터레스트 접속
    URL = "https://www.pinterest.co.kr/search/pins/?q={}".format(keyword)
    driver.get(URL)
    for i in range(page_D):
        all_of_them(driver,i,keyword)
    driver.close()
