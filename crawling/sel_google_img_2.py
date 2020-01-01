from selenium import webdriver
import time
from tqdm import tqdm

def link_cl(driver):    #이미지 링크 수집
    imgs = driver.find_elements_by_css_selector('a.rg_l')
    print(imgs)
    # result = []
    # for img in imgs:
    #     img.click()
    #     time.sleep(1)


keyword = input("찾고싶은 이미지 검색 : ")

#셀레니움 설정
option = webdriver.ChromeOptions()
option.add_argument('--disable-gpu')
option.add_argument('lang=ko')

driver = webdriver.Chrome('chromedriver',options=option)
driver.implicitly_wait(3)

# 구글 이미지 검색 사이트 이동
URL = "https://www.google.com/search?q={}&sxsrf=ACYBGNSenINKmLnHzAPJKXO-AhYzReACRQ:1576128347890&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiXg6_Sr6_mAhWRyosBHV9eB3EQ_AUoAXoECBMQAw&biw=958&bih=959".format(keyword)
driver.get(URL)

# 페이지 스크롤
# page_dw(keyword,driver)


# 이미지 링크 수집
imgs = link_cl(driver)
























# def mk_zip(keyword):    #얍축
#     import os
#     import zipfile
#     zip_file = zipfile.ZipFile('./google_{}.zip'.format(keyword), 'w')
#
#     for image in os.listdir('./google_{}'.format(keyword)):
#         zip_file.write('./google_{}/{}'.format(keyword,image), compress_type = zipfile.ZIP_DEFLATED)
#     zip_file.close()
#     print("압축완료")
