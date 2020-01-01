from selenium import webdriver
from urllib.request import urlopen
import time
from tqdm import tqdm


def get_insta_img(keyword):
    page_D = int(input("페이지 다운 횟수 : "))
    driver = webdriver.Chrome()
    insta_login(driver)
    URL = "https://www.instagram.com/explore/tags/{}/".format(keyword)
    driver.get(URL)
    page_dw(keyword,driver,page_D)
    # mk_zip(keyword)
    # driver.close()

def insta_login(driver):
    URL = "https://www.instagram.com/accounts/login/"
    driver.get(URL)
    time.sleep(3)
    driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input').send_keys('jinho971031')
    driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input').send_keys('KJHwhsgh9(')
    driver.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4) > button').click()
    time.sleep(3)

def page_dw(keyword,driver,page_D):    #페이지 스크롤 다운,5페이지마다 이미지 다운로드
    from selenium.webdriver.common.keys import Keys
    body = driver.find_element_by_css_selector('body')
    Down = range(page_D // 7)
    for i in range(page_D):
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        if(i%5==0):
            time.sleep(3)
            links = link_cl(driver)
            mkdir_dw(keyword,links,Down)

def link_cl(driver):    #이미지 링크 수집
    imgs = driver.find_elements_by_css_selector('img')
    result = []
    for img in imgs:
        result.append(img.get_attribute('src'))
    return result

def mkdir_dw(keyword,links,Down):    #폴더생성, 다운로드
    import os
    last_in = 0
    if not os.path.isdir('./insta_{}'.format(keyword)):
        os.mkdir('./insta_{}'.format(keyword))
    #다운로드 시작
    from urllib.request import urlretrieve

    for idx in Down:
        for index, link in tqdm(enumerate(links)):
        #rfind : 끝에서 부터 찾아주는 함수
            end = link.rfind('?')
            start = link.rfind('_n.')
            #print(link[start:end])
            filetype = link[start:end]
            urlretrieve(link, './insta_{}/{}{}-{}{}'.format(keyword,keyword,idx,index,filetype))
            last_in = index

        print(f'{idx}페이지 다운로드 완료')


def mk_zip(keyword):    #얍축
    import os
    import zipfile
    zip_file = zipfile.ZipFile('./insta_{}.zip'.format(keyword), 'w')

    for image in os.listdir('./insta_{}'.format(keyword)):
        zip_file.write('./insta_{}/{}'.format(keyword,image), compress_type = zipfile.ZIP_DEFLATED)
    zip_file.close()
    print("압축완료")
