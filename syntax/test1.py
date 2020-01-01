from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

html = urlopen("https://www.youtube.com/feed/trending")
bsObject = BeautifulSoup(html, "html.parser")

result = bsObject.head.title

print(result)
