# 这是Python2016/Python实战：：四周实现爬虫系统第一周课时13的学习

from bs4 import BeautifulSoup
from urllib import request

# url = "http://weibo.com/u/2682207107/home?topnav=1&wvr=6"
# headers = {
#     'Cookie': 'YF-V5-G0=cd5d86283b86b0d506628aedd6f8896e; YF-Ugrow-G0=ad06784f6deda07eea88e095402e4243; _s_tentry=-; Apache=27634262696.427658.1487043599348; SINAGLOBAL=27634262696.427658.1487043599348; ULV=1487043599656:1:1:1:27634262696.427658.1487043599348:; login_sid_t=1679c7e1cfba9357e93947a9aa7ab933; YF-Page-G0=b9004652c3bb1711215bacc0d9b6f2b5; UM_distinctid=15b4bb7ef7872-08add0405c49e3-58133915-100200-15b4bb7ef7b280; wb_publish_fist100_2682207107=1; TC-V5-G0=8518b479055542524f4cf5907e498469; SSOLoginState=1491841861; WBtopGlobal_register_version=a05309c5d15974a8; TC-Page-G0=cdcf495cbaea129529aa606e7629fea7; wvr=6; SCF=AtG303etTSzpp_SZpFLwp8WAco5HV87nF_Ht--9gQZk0_PvWffHAVz3H8vwrN1fIJD6yihRatToCYC2JvIda75I.; SUB=_2A250DsY3DeRhGeRI41AT8CnNyzuIHXVXfbD_rDV8PUNbmtBeLW7skW8sdAgWnBQ-B2kAurP64Q0mlFk2jw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhujdPx2yD8HVfG-r3fsWXm5JpX5KMhUgL.Fozc1hzEehMpehM2dJLoIfUeIgSQ9g-LxKBLB.zL122LxK-LBKBLBK.LxKqL1h.LB.-LxK-L1hnLBo5LxK-LBK-LBoeLxKqL1-eL12zLxK-L12qL12zLxKBLB.2L1hqLxK-L1K5L1KMt; SUHB=03oEfIzFKsuIEL; ALF=1525410277; UOR=,,login.sina.com.cn',
#     'Host': 'weibo.com',
#     'Referer': 'http://weibo.com/u/2682207107/home?topnav=1&wvr=6',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest'
# }
# req = request.Request(url,headers=headers)
# wb_data = request.urlopen(req).read()
# soup = BeautifulSoup(wb_data, 'lxml')
#
# print(soup)

url = 'https://knewone.com/discover?page=7'
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

'''
#wrapper > div > section > div:nth-child(1) > div.hits_group-things.clearfix > article:nth-child(2) > header > a > img
#wrapper > div > section > div:nth-child(1) > div.hits_group-things.clearfix > article:nth-child(3) > header > a > img
'''

def get_page(url,headers=headers,data=None):
    req = request.Request(url,headers=headers)
    wb_data = request.urlopen(req).read()
    soup = BeautifulSoup(wb_data,'lxml')
    # imgs = soup.select('div.hits_group-things.clearfix > header > a > img')
    titles = soup.select('section.content > h4 > a')
    # links = soup.select('a.unfancied > data-link')
    # print(url, headers, data,req,wb_data,soup,imgs,titles,links, sep="\n*********************\n")
    print(titles)
    if data==None:
        for title in zip(titles):
            data = {
                'title':title[0].get('title')
            }
            print(data['title'])
get_page(url)
