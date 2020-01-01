from selenium import webdriver
import time
from tqdm import tqdm
import requests


def google_login(driver):   #구글 로그인
    URL = "https://accounts.google.com/"
    driver.get(URL)
    time.sleep(1)
    driver.find_element_by_css_selector('#identifierId').send_keys('jinho971031')
    driver.find_element_by_css_selector('#identifierNext > span > span').click()
    time.sleep(1)
    driver.find_element_by_css_selector('#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input').send_keys('KJHwhsgh9(')
    driver.find_element_by_css_selector('#passwordNext > span > span').click()
    time.sleep(3)


def page_dw(keyword,driver):    #페이지 스크롤 다운,5페이지마다 이미지 다운로드
    from selenium.webdriver.common.keys import Keys
    body = driver.find_element_by_css_selector('body')
    x = 0
    while(True):
        for i in range(11):
            body.send_keys(Keys.PAGE_DOWN)
            body.send_keys(Keys.PAGE_DOWN)
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        if x is 1:
            break
        time.sleep(1)
        driver.find_element_by_css_selector('#smb').click()
        x += 1


def link_cl(driver):    #이미지 링크 수집
    imgs = driver.find_elements_by_xpath('//*[@id="rg_s"]/div/a')

    result = []
    for img in imgs:
        if 'imgres' in img.get_attribute('href'):
            result.append(img.get_attribute('href'))
    return result


def get_img_in_page(driver,links,count,keyword):  # 링크 접속 후 이미지 소스 추출
    print("이미지 추출중")
    results = []
    i = 0


    for link in links:
        if(i==count):
            break
        driver.get(link)
        time.sleep(1)
        imgs = driver.find_elements_by_css_selector('img.irc_mi')

        for img in imgs:
            if img.get_attribute('src') is not None:
                results.append(img.get_attribute('src'))
        i+=1

    get_img(keyword,results)


def get_img(keyword,img_srcs):    #폴더생성, 다운로드
    import os
    # 디렉토리 생성
    if not os.path.isdir('./google_{}'.format(keyword)):
        os.mkdir('./google_{}'.format(keyword))

    # 다운로드 시작
    from urllib.request import urlretrieve

    for index, src in tqdm(enumerate(img_srcs)):
        # 파일타입지정
        if '.jpg' in src:
            filetype = '.jpg'
        elif '.png' in src:
            filetype = '.png'
        elif '.gif' in src:
            filetype = '.gif'
        else:
            continue

        savename = f'./google_{keyword}/{keyword}{index}{filetype}'
        mem=requests.get(src, verify=False).content
        with open(savename, "wb") as f:    #바이너리(이미지)일 경우 'wb',  텍스트일 경우 'w'
            f.write(mem)
        time.sleep(1)


def get_google_img(keyword):
    # header={'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

    #셀레니움 설정

    option = webdriver.ChromeOptions()
    # 랜덤으로 생성한 UserAgent 값을 출력한다
    # ua = UserAgent(verify_ssl=False)
    # userAgent = ua.random
    # print(userAgent)
    # 생성한 UserAgent 값을 옵션에 추가한다
    # option.add_argument(f'user-agent={userAgent}')
    option.add_argument(f"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    option.add_argument('--disable-gpu')
    option.add_argument('lang=ko')

    driver = webdriver.Chrome('chromedriver',options=option)
    driver.implicitly_wait(3)


    # 구글 로그인
    google_login(driver)


    # 구글 이미지 검색 사이트 이동
    URL = "https://www.google.com/search?q={}&sxsrf=ACYBGNSenINKmLnHzAPJKXO-AhYzReACRQ:1576128347890&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiXg6_Sr6_mAhWRyosBHV9eB3EQ_AUoAXoECBMQAw&biw=958&bih=959".format(keyword)
    driver.get(URL)

    # 페이지 스크롤
    page_dw(keyword,driver)


    # 이미지 링크 수집
    imgs = link_cl(driver)


    # 비어있는 주소 처리
    links = []
    for img in imgs:
        if img is not None:
            links.append(img)

    count = int(input("{}개의 이미지를 찾았습니다. 몇개의 이미지를 찾으시겠습니까? : ".format(len(links))))
    # 링크 접속 후 이미지
    get_img_in_page(driver,links,count,keyword)
    driver.close()
























# def mk_zip(keyword):    #얍축
#     import os
#     import zipfile
#     zip_file = zipfile.ZipFile('./google_{}.zip'.format(keyword), 'w')
#
#     for image in os.listdir('./google_{}'.format(keyword)):
#         zip_file.write('./google_{}/{}'.format(keyword,image), compress_type = zipfile.ZIP_DEFLATED)
#     zip_file.close()
#     print("압축완료")
