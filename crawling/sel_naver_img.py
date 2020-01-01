from selenium import webdriver
from urllib.request import urlopen
import time
from tqdm import tqdm

def get_naver_img(keyword):
    page_D = int(input("페이지 다운 횟수 : "))
    driver = webdriver.Chrome()
    URL = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query={}".format(keyword)
    driver.get(URL)
    page_dw(driver,page_D)
    links = link_cl(driver)
    mkdir_dw(keyword,links)
    # 압축
    # mk_zip(keyword)
    driver.close()

def page_dw(driver,page_D):    #페이지 스크롤 다운
    from selenium.webdriver.common.keys import Keys
    body = driver.find_element_by_css_selector('body')
    for i in range(page_D):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

def link_cl(driver):    #이미지 링크 수집
    imgs = driver.find_elements_by_css_selector('img._img')
    result = []
    for img in tqdm(imgs):
        if 'http' in img.get_attribute('src'):
            result.append(img.get_attribute('src'))
    print('수집 완료')
    return result

def mkdir_dw(keyword,links):    #폴더생성, 다운로드
    import os
    if not os.path.isdir('./{}'.format(keyword)):
        os.mkdir('./{}'.format(keyword))
    #다운로드 시작
    from urllib.request import urlretrieve
    for index, link in tqdm(enumerate(links)):
    #rfind : 끝에서 부터 찾아주는 함수
        start = link.rfind('.')
        end = link.rfind('&')
        #print(link[start:end])
        filetype = link[start:end]
        urlretrieve(link, './{}/{}{}{}'.format(keyword,keyword,index,filetype))
    print('다운로드 완료')

def mk_zip(keyword):    #얍축
    import os
    import zipfile
    zip_file = zipfile.ZipFile('./{}.zip'.format(keyword), 'w')

    for image in os.listdir('./{}'.format(keyword)):
        zip_file.write('./{}/{}'.format(keyword,image), compress_type = zipfile.ZIP_DEFLATED)
    zip_file.close()
    print("압축완료")
