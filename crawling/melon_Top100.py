import urllib.request
from bs4 import BeautifulSoup
import csv

hdr = { 'User-Agent' : 'Mozilla/5.0' }
url = "https://www.melon.com/chart/index.htm"
url2 = "https://www.melon.com/chart/index.htm#params%5Bidx%5D=51"

req = urllib.request.Request(url, headers=hdr)

result = urllib.request.urlopen(req).read()
soup = BeautifulSoup(result, 'html.parser')
# list50 = soup.select('.lst50')
lists = soup.select('.lst50,.lst100')

#print(list50)

def get_melon_chart():
    charts = []
    for lst in lists:
        chart = get_chart_info(lst)
        charts.append(chart)
    save_to_file(charts)


def get_chart_info(html):
    rank = html.find('span',{'class':'rank'})
    rank = rank.string
    rank = rank.strip()
    title = html.find('div',{'class':'rank01'}).a.text
    singer = html.find('div',{'class':'rank02'}).a.text
    albem = html.find('div',{'class':'rank03'}).a.text
    return {
    'rank':rank,
    'title':title,
    'singer':singer,
    'albem':albem
    }

def save_to_file(charts):
    file = open("charts.csv", mode="w", newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(["rank","title","singer","albem"])

    for chart in charts:
        writer.writerow(list(chart.values()))
    return
