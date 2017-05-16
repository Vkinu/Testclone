# coding=utf-8
import urllib
import re
import time
import cookielib
import urllib2
import wget
import requests
from lxml import etree
# #创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie3.txt', ignore_discard=True, ignore_expires=True)
r = str(int(round(time.time() * 1000)))
#创建请求的request
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    "Referer" : "http://www.xiami.com/song/bpVOa3dc7?spm=a1z1s.6626001.229054121.2.YUCnCX",
    "X-Requested-With" : "XMLHttpRequest",
    "Host" : "www.xiami.com",
    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}
proxy = {'http':'180.97.235.30:80'}
proxy_support = urllib2.ProxyHandler(proxy)
q=1
id1 = 1795888147
id = str(id1)
i=0


req = urllib2.Request("http://www.xiami.com/download/get-link?_=" + r + "&type=song&id=" + id + "&quality=1",
                      headers=header)

req2 = urllib2.Request(
    "http://www.xiami.com/download/get-link?ping=1&_=" + r + "&type=song&id=" + id + "&quality=1",
    headers=header)
time.sleep(3)
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(proxy_support,urllib2.HTTPCookieProcessor(cookie))


reqid = urllib2.Request("http://www.xiami.com/song/xNdulbc1e05?spm=a1z1s.6659513.0.0.uZQJJd",
                      headers=header)
responseid = opener.open(reqid).read()

html = etree.HTML(responseid)
resulttitle = html.xpath('//html/head/meta[10]/@content')
title = resulttitle[0].encode("utf8")
print title
resulturl = html.xpath('//html/head/meta[12]/@content')
id2 = resulturl[0][48:]
# print id
#
# id = str(id2)



response2 = opener.open(req2)
response = opener.open(req)
result = response2.read()
result2 = result.replace("\\", '')
print result2
pattern2 = re.compile(r'http:.*"')
try:
    mattch2 = re.search(pattern2, result2).group()[:-1]
    print mattch2
    response3 = opener.open(mattch2)
    stream = response3.read()
    f = open('c:\\IMG\\' + title + '.mp3', 'wb')
    f.write(stream)
    f.close()
    s = 1
    print "完成啦"
except:
    i = i + 0
    s = 0
while s == 0:
    time.sleep(1)
    req = urllib2.Request("http://www.xiami.com/download/get-link?_=" + r + "&type=song&id=" + id + "&quality=1",
                          headers=header)

    req2 = urllib2.Request(
        "http://www.xiami.com/download/get-link?ping=1&_=" + r + "&type=song&id=" + id + "&quality=1",
        headers=header)
    time.sleep(3)
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response2 = opener.open(req2)
    response = opener.open(req)
    result = response2.read()
    result2 = result.replace("\\", '')
    print result2
    pattern2 = re.compile(r'http:.*"')
    try:
        mattch2 = re.search(pattern2, result2).group()[:-1]
        print mattch2
        response3 = opener.open(mattch2)
        stream = response3.read()
        f = open('c:\\IMG\\' + title + '.mp3', 'wb')
        f.write(stream)
        f.close()
        s = 1
    except:
        i = i + 0
        s = 0
        if s == 1:
            break
























