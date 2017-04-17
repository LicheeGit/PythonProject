# 这是Python实战：：四周实现爬虫系统_第一周的练习
# 解析真实世界中的网页

from bs4 import BeautifulSoup
from urllib import request
url = "http://www.mafengwo.cn/mdd/route/10926.html"
wb_data = request.urlopen(url)
soup = BeautifulSoup(wb_data.read(),'lxml')
# print(soup)
titles = soup.select("div.days-season > span")
print(titles)
