# 这是传智播客2016视频DAY12-13的学习

from urllib import request
from bs4 import BeautifulSoup
response = request.urlopen("https://mp.weixin.qq.com/")
html = response.read()
soup = BeautifulSoup(html,"lxml")
# print(soup.prettify())
# print(soup.title)
# print(soup.head)
print(type(soup.a))
print(soup.p.attrs)
print(soup.p.get('class'))
print(soup.p.string)

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# 添加一个解析器
soup = BeautifulSoup(html, 'html5lib')
print(soup.title)
print(soup.title.name)
print(soup.title.text)
print(soup.body)

# 从文档中找到所有<a>标签的内容
for link in soup.find_all('a'):
    print(link.get('href'))

# 从文档中找到所有文字内容
print(soup.get_text())

