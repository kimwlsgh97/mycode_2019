from sel_naver_img import get_naver_img
from sel_insta_img import get_insta_img
from sel_google_img import get_google_img
from sel_bing_img import get_bing_img
from sel_pint_img import get_pint_img

# from melon_Top100 import get_melon_chart
# from jobkor import get_JOBkor_Job

def img_scrap():
    keyword = input("찾고싶은 이미지 검색 : ")
    choise = input("사용하실 검색엔진의 번호를 선택하세요. (1:네이버,2:인스타,3:구글,4:빙,5:핀터레스트) : ")

    if (choise is '1'):
        get_naver_img(keyword)
    if (choise is '2'):
        get_insta_img(keyword)
    if (choise is '3'):
        get_google_img(keyword)
    if (choise is '4'):
        get_bing_img(keyword)
    if (choise is '5'):
        get_pint_img(keyword)
