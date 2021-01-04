''' 
本次提交的作业，并没有实现，模拟知乎登录手机登录的功能。仅实现了作为游客，进行数据抓取的功能
后期仍然需要优化的2点:
①模拟知乎登录后，然后进行数据抓取【我的账号，仅支持，手机发送验证码的登录方式】
②爬取全部数据的时候，可采用多线程的方式
③代码后期需要进行调优


老师给的几点建议，使用
①要解决的是cookie问题，而知乎post用户密码是加密的可以采用调用知乎的js加密密码提交，也可以采用selenium模拟浏览器登陆成功一次拿到cookie再继续用requests做自动化操作，其他大家可以讨论
②关于JS加密密码提交方式，参考：知乎的js加密密码提交，老师能否再解释的仔细一点呢。https://www.zhihu.com/tardis/sogou/art/32898234?ab_signature=CiRBUEJneXFtV3ZROUxCZThtLXZ2M2VmcV9YZ0k3Znczclcwaz0SIDU1MWQ0YzllY2JjNDE3ZmMxYWJmMDk5NzU5NmE4ZWZiGhAIARIGNi42OS4xGgQzNDYw

'''

import requests
import lxml
from bs4 import BeautifulSoup
import os
from pathlib import *


def getCurrentPageData(currentUrl, headers, filePath):
    list1 = []
    r = requests.get(currentUrl, headers=headers)

    with open(filePath, 'w', encoding="UTF-8") as file:
        file.write(r.text)

    soup = BeautifulSoup(open(filePath, encoding="UTF-8"), 'lxml')

    for title_href in soup.find_all('div', class_='SpecialListCard-infos'):
        for title in title_href.find_all('a'):
            if title.string is not None:
                list1.append(title.string)

    return list1


def getMorePageData(pageMoreUrl, headers):
    r1 = requests.get(pageMoreUrl, headers=headers)
    list1 = []

    for i in r1.json()["data"]:
        if "title" in i:
            list1.append(i["title"])

    return list1


if __name__ == '__main__':
    path = os.getcwd()
    a = Path(path)
    filePath = a.joinpath("crawl_content.html")

    currentUrl = "https://www.zhihu.com/special/all"

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    list1 = getCurrentPageData(currentUrl, headers, filePath)

    list3 = []

    for i in range(50):
        pageMoreUrl = f"https://www.zhihu.com/api/v4/news_specials/list?limit=10&offset={10*(i+1)}"
        # print(pageMoreUrl)
        list2 = getMorePageData(pageMoreUrl, headers)
        for i in list2:
            list3.append(i)

    for i in list1 + list3:
        print(f'序号是:{(list1 + list3).index(i)} 对应抓取的值:{i}')
