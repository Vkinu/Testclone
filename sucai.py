# coding=utf-8
import urllib
import urllib2
import re
import cStringIO
from PIL import Image
from lxml import etree
import time
j=123510
ss = 1
for i in range(1000):
    try:
        f = str(j)
        url = "http://www.16sucai.com/2017/05/" + f + ".html"
        request = urllib2.Request(url)
        res = urllib2.urlopen(request).read()
        html = etree.HTML(res)
        result = html.xpath('//p/a/img/@src')
        for i in result:
            print i
            s = j
            urllib.urlretrieve(i, 'c:\\IMG\\%s.jpg' % s)
        j = j + 1
    except :
        j=j+1
        print u"不行加1"
        



