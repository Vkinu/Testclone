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
proxy = {'http':'49.82.165.223:8998'}
proxy_support = urllib2.ProxyHandler(proxy)

# id1 = 1795888147
# id = str(id1)



# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(proxy_support,urllib2.HTTPCookieProcessor(cookie))
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
reqid = urllib2.Request("http://www.xiami.com/song/kab9d26ff?spm=a1z1s.6659509.0.0.Eo4mhW",
                      headers=header)
responseid = opener.open(reqid).read()

html = etree.HTML(responseid)
resulttitle = html.xpath('//html/head/meta[10]/@content')
title = resulttitle[0].encode("utf8")
print title
resulturl = html.xpath('//html/head/meta[12]/@content')
id2 = resulturl[0][48:]
print id2
# 循环次数
count = 10
w = 1
for w in range(count):
    id2 = int(id2) + 1
    id = str(id2)
    print id
    req = urllib2.Request("http://www.xiami.com/download/get-link?_=" + r + "&type=song&id=" + id + "&quality=1",
                          headers=header)
    req2 = urllib2.Request(
        "http://www.xiami.com/download/get-link?ping=1&_=" + r + "&type=song&id=" + id + "&quality=1",
        headers=header)
    time.sleep(3)
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
        # title21=int(time.time()*1000)
        # title2= title.decode('unicode-escape')
        title2 = unicode(title, "utf-8")
        title4 = str(int(round(time.time() * 1000)))
        title222 = "c:\\IMG\\" + title4 + ".mp3"
        f = open(title222, 'wb')
        f.write(stream)
        f.close()
        s = 1
        w = w + 1
        print "完成啦"
    except:

        s = 0
        print "再来一次把"
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
            title4 = str(int(round(time.time() * 1000)))
            f = open('c:\\IMG\\' + title4 + '.mp3', 'wb')
            f.write(stream)
            f.close()
            s = 1
            w = w + 1
            print "还好继续完成啦"
        except:
            s = 0
            if s == 1:
                break
            print "在执行几次"


# print id
#
























