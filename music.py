#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib
import re
import time
import cookielib
import urllib2
import wget
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
# driver = webdriver.Chrome()
imageUrl="http://download.file.xiami.com/download/get?id=1008716&type=song&quality=1&crc=c0182098ac78cee07a84bcf813649e8e"

loginUrl = 'http://www.xiami.com/song/xNbdb0dbb30?spm=a1z1s.3521865.23309997.1.Ebyoym'  # 登录教务系统的URL，成绩查询网址
# #创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie3.txt', ignore_discard=True, ignore_expires=True)
#创建请求的request
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Referer" : "http://www.xiami.com/song/xNbdb0dbb30?spm=a1z1s.3521865.23309997.1.Ebyoym",
}
req2 = urllib2.Request("http://www.xiami.com/download/get-link?_=1494835079916&type=song&id=1008716&quality=1",headers=header)

req = urllib2.Request("http://www.xiami.com/download/get-link?ping=1&_=1494835081916&type=song&id=1008716&quality=1",headers=header)

req3 =urllib2.Request("http://download.file.xiami.com/download/get?id=1008716&type=song&quality=1&crc=c0182098ac78cee07a84bcf813649e8e")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)
response2 = opener.open(req2)
print response.read()
print response2.read()
response3 = opener.open(req3)
# print response.read()
# print response2.read()
# # print response3.read()
#
#
#
# driver.get(imageUrl)
urllib.urlretrieve('https://baike.baidu.com/pic/Python/407313/0/0eb30f2442a7d9331abfc6f3ad4bd11373f0011e?fr=lemma&ct=single#aid=0&pic=0eb30f2442a7d9331abfc6f3ad4bd11373f0011e', 'C:/BingYu.jpg')
# urllib.urlretrieve("http://download.file.xiami.com/download/get?id=1008716&type=song&quality=1&crc=c0182098ac78cee07a84bcf813649e8e", u"平哥aaaa.mp3")
# # baseurl = "http://music.baidu.com"
# # url = "http://music.baidu.com/search/tag?key=经典流行"
# # html = urllib.urlopen(url).read()
# # uri = re.findall(r'/song/\d+', html, re.M)
# # lst = []
# # print lst
# # for i in uri:
# #     link = baseurl+i+"/download"
# #     lst.insert(0, link)
# # for k in lst:
# #     res = urllib.urlopen(k).read()
# #     down = re.search('http://[^ ]*xcode.[a-z0-9]*' , res, re.M).group()
# #     s1 = re.search('title=".*',res, re.M).group()
# #     s2 = re.search('>.*<.a', s1, re.M).group()
# #     s3 = s2[1:-3]
# #     print s3
# #     down="http://music.baidu.com/song/100575177"
# #     urllib.urlretrieve(down, s3+".mp3")
#
# down="http://music.baidu.com/song/100575177"
# s3=int(time.time())
# s4=str(s3)
# urllib.urlretrieve(down, u"我很棒"+s4+".mp3")