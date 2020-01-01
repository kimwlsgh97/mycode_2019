import requests
from bs4 import BeautifulSoup
import csv

keyword = input("잡코리아에 검색할 직업을 입력하세요 : ")
pg_num = 1
url = "http://www.jobkorea.co.kr/Search/?stext={}&tabType=recruit&Page_No={}".format(keyword,pg_num)

def get_JOBkor_Job():
    last_pg = get_last_page()
    jobs = get_page_info(last_pg)
    save_to_file(jobs)

def get_last_page():
    result = requests.get(url)
    soup = BeautifulSoup(result.text,"html.parser") # HTML 텍스트를 직접 전달
    # lists = soup.select('.list-post')
    page_link = soup.select('.pgTotal')
    last_page = int(page_link[0].string)
    return last_page

def get_page_info(last_pg):
    jobs = []
    for pg in range(last_pg):
        print(f"{pg+1}번째 페이지 스크롤.")
        pg_num = pg
        result = requests.get(url)
        soup = BeautifulSoup(result.content,"html.parser")
        infos = soup.select('.post')
        for info in infos:
            job = get_job_info(info)
            if job["title"] is not None:
                jobs.append(job)
    return jobs

def get_job_info(info):
    company = info.select_one('a.name.dev_view')
    if company is not None:
        company = info.select_one('a.name.dev_view')["title"]

    title = info.select_one('a.title.dev_view')
    if title is not None:
        title = info.select_one('a.title.dev_view')["title"]

    exp = info.select_one('span.exp')
    if exp is not None:
        exp = info.select_one('span.exp').string

    edu = info.select_one('span.edu')
    if edu is not None:
        edu = info.select_one('span.edu').string

    position = info.find('span',{'class':None})
    if position is not None:
        position = info.find('span',{'class':None}).string

    date = info.select_one('span.date')
    if date is not None:
        date = info.select_one('span.date').string

    link = info.select_one('a.name.dev_view')
    if link is not None:
        link = info.select_one('a.name.dev_view')["href"]

    return {
    'company':company,
    'title':title,
    'exp':exp,
    'edu':edu,
    'position':position,
    'date':date,
    'link':f"http://www.jobkorea.co.kr{link}"
    }

def save_to_file(jobs):
    file = open("job_{}.csv".format(keyword), mode="w", newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(["company","title","exp","edu","position","date","link"])

    for job in jobs:
        writer.writerow(list(job.values()))
    return

get_JOBkor_Job()
