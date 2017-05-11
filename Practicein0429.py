# 这是Python2016/Python实战：：四周实现爬虫系统第一周课时13的学习

from bs4 import BeautifulSoup
from urllib import request

'''
https://www.lagou.com/zhaopin/Python/?labelWords=label
https://www.lagou.com/zhaopin/Python/2/?filterOption=2
https://www.lagou.com/zhaopin/Python/2/?filterOption=3
https://www.lagou.com/zhaopin/Python/3/?filterOption=3
https://www.lagou.com/zhaopin/Python/?filterOption=3
'''
url = 'https://www.lagou.com/zhaopin/Python/?labelWords=label'
# print(url)
headers = {
'Connection':'keep-alive',
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
info = []
data = None
req = request.Request(url,headers=headers)
wb_data = request.urlopen(req).read()
soup = BeautifulSoup(wb_data.decode('UTF-8'), 'lxml')
# print(soup)
imgs = soup.select('img[width="60"]')
# imgs = soup.select('div.list_item_top > div.com_logo > a > img')
titles = soup.select('div.list_item_top > div.position > div.p_top > a > h2')
cates = soup.select('div.list_item_bot > div.li_b_l ')
#s_position_list > ul > li:nth-child(4) > div.list_item_top > div.com_logo > a > img
# print(wb_data.decode('UTF-8'))
# print(imgs)
for img,title,cate in zip(imgs, titles,cates):
    data = {
        'img': img['src'],
        'title': title.get_text(),
        'cate':list(cate.stripped_strings)
        # 'title': title.get('title'),
        # 'link': link.get('href')
    }
    print(data)
#     info.append(data)
# for i in info:
#     if i['title']=='Python':
#         print(i['title'],i['img'],i['cate'])
