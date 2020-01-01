from selenium import webdriver
import time
from tqdm import tqdm
# hdr = { 'User-Agent' : 'Mozilla/5.0' }
import requests

def page_dw(driver,page_D):    #페이지 스크롤 다운
    from selenium.webdriver.common.keys import Keys
    body = driver.find_element_by_css_selector('body')
    for i in range(page_D):
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)


def link_cl(driver):    #이미지 링크 수집
    imgs = driver.find_elements_by_css_selector('a.iusc')
    result = []
    for img in imgs:
        result.append(img.get_attribute('href'))
    return result


def get_img_in_page(driver,links,count,keyword):  # 링크 접속 후 이미지 소스 추출
    print("이미지 추출중")
    results = []
    i = 0
    for link in tqdm(links):
        if i is count:
            break
        driver.get(link)
        time.sleep(1)
        img = driver.find_element_by_xpath('//*[@id="mainImageWindow"]/div[1]/div/div/div/img')
        results.append(img.get_attribute('src'))
        i += 1
    get_img(keyword,results)


def get_img(keyword,img_srcs):    #폴더생성, 다운로드
    import os
    # 디렉토리 생성
    if not os.path.isdir('./bing_{}'.format(keyword)):
        os.mkdir('./bing_{}'.format(keyword))
        filetype = ''
        # 다운로드 시작
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

            savename = f'./bing_{keyword}/{keyword}{index}{filetype}'
            mem=requests.get(src, verify=False).content
            with open(savename, "wb") as f:    #바이너리(이미지)일 경우 'wb',  텍스트일 경우 'w'
                f.write(mem)
            time.sleep(1)


def get_bing_img(keyword):
    page_D = int(input("페이지 다운 횟수 : "))

    # 구글 로그인
    driver = webdriver.Chrome()

    # 구글 이미지 검색 사이트 이동
    URL = "https://www.bing.com/images/search?q={}".format(keyword)
    driver.get(URL)
    # 페이지 스크롤
    page_dw(driver,page_D)

    # 이미지 링크 수집
    imgs = link_cl(driver)

    # 비어있는 주소 처리
    links = []
    for img in imgs:
        if img is not None:
            links.append(img)

    count = int(input(f"{len(links)}개의 이미지를 찾았습니다. 몇개의 이미지를 찾으시겠습니까? : "))
    # 링크 접속 후 이미지
    get_img_in_page(driver,links,count,keyword)
    driver.close()























# def page_dw(keyword,driver):    #페이지 스크롤 다운,5페이지마다 이미지 다운로드
#     from selenium.webdriver.common.keys import Keys
#     body = driver.find_element_by_css_selector('body')
#     x = 0
#     while(True):
#         for i in range(11):
#             body.send_keys(Keys.PAGE_DOWN)
#             body.send_keys(Keys.PAGE_DOWN)
#             body.send_keys(Keys.PAGE_DOWN)
#             time.sleep(1)
#         if x is 1:
#             break
#         time.sleep(1)
#         driver.find_element_by_css_selector('#smb').click()
#         x += 1

# def mk_zip(keyword):    #얍축
#     import os
#     import zipfile
#     zip_file = zipfile.ZipFile('./google_{}.zip'.format(keyword), 'w')
#
#     for image in os.listdir('./google_{}'.format(keyword)):
#         zip_file.write('./google_{}/{}'.format(keyword,image), compress_type = zipfile.ZIP_DEFLATED)
#     zip_file.close()
#     print("압축완료")
