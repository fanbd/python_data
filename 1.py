"""
抓取网页上的绿色文字
http://www.pythonscraping.com/pages/warandpeace.html
<span class="green">
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())
