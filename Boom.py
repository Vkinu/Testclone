# coding=utf-8
import cookielib
import urllib2,time,urllib
# 创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
req = urllib2.Request("http://www.lenovo.com.cn/index.html")
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)

mobile = '15958124631'
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Referer" : "http://www.lenovo.com.cn/index.html"
}
r = str(int(round(time.time() * 1000)))
data1 = urllib.urlencode({
    'mobile': mobile,
    'callback':'response.getMobileCaptCode',
    '_' :r
})
url1 = "http://reg.lenovo.com.cn/captcha/mobile/show?"+data1
Request = urllib2.Request(url1,headers=header)
Res = opener.open(Request)
# Res = urllib2.urlopen(Request)
print Res.read()

#牛逼接口 传化物流+++
for i in range(5):
    # 创建MozillaCookieJar实例对象
    cookie = cookielib.MozillaCookieJar()
    # 从文件中读取cookie内容到变量
    cookie.load('mycookies2.txt', ignore_discard=True, ignore_expires=True)
    # 创建请求的request
    req = urllib2.Request(
        "http://www.tf56.com/site/regcs/sendSmsValidateCodeByMobile?random=0.3602049623509711&_tf_token_=Z4u1uFYw3Yq")
    # 利用urllib2的build_opener方法创建一个opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    opener.addheaders = [("User-Agent",
                          "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36")]
    opener.addheaders = [("Referer", "http://www.tf56.com/site/partycentercs/signUp?skipBack=http://www.tf56.com/")]
    urllib2.install_opener(opener)

    data23 = urllib.urlencode({
        '': '',
        'type': 'PC的注册',
        'mobilenumber': mobile,
        'shortnumber': '123'
    })
    url2 = "http://www.tf56.com/site/regcs/sendSmsValidateCodeByMobile?random=0.3602049623509711&_tf_token_=Z4u1uFYw3Yq"
    Request2 = urllib2.Request(url2, data23)
    Res2 = opener.open(Request2)
    # Res = urllib2.urlopen(Request)
    print Res2.read()
    time.sleep(5)

#金蝶云

#嘉禾易送 只能一条
# 创建MozillaCookieJar实例对象
cookie = cookielib.MozillaCookieJar()
# 从文件中读取cookie内容到变量
cookie.load('cookie3.txt', ignore_discard=True, ignore_expires=True)
# 创建请求的request
req = urllib2.Request("http://www.esoon360.cn/account/send_sms.shtml")
# 利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

url3 = "http://www.esoon360.cn/account/send_sms.shtml"
header3 = {
    "Referer":"http://www.esoon360.cn/account/register.shtml",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36"
}
data3  = urllib.urlencode({
    'phone': '15958124631'
})
Request3 = urllib2.Request(url3,headers=header3,data=data3)
Res3 = opener.open(Request3)
print Res3.read()


to="15958124631"
url = "https://api.mysubmail.com/message/xsend"
data = urllib.urlencode({
    "appid":"13880",
    "to":to,
    "project":"u6FBI2",
    "signature":"115abba773b0f1fa150f3ee567959085"
})
Request = urllib2.Request(url,data)
Res = urllib2.urlopen(Request)
print (Res.read())


url = "https://api.mysubmail.com/message/xsend"
data = urllib.urlencode({
    "appid":"13876",
    "to":to,
    "project":"eNAp32",
    "signature":"c473a6be34554fb12341a8f74f083096"
})
Request = urllib2.Request(url,data)
Res = urllib2.urlopen(Request)
print (Res.read())

url2 = "https://api.mysubmail.com/voice/verify.json"
data2 = urllib.urlencode({
    "appid":"20306",
    "to":to,
    "code":"6666666666",
    "signature":"920519e2a6a445131b3122745b263416"
})
Request2 = urllib2.Request(url2,data2)
Res2 = urllib2.urlopen(Request2)
print (Res2.read())



url3 = "https://api.mysubmail.com/voice/verify.json"
data3 = urllib.urlencode({
    "appid":"20307",
    "to":to,
    "code":"8888888",
    "signature":"4a7ba598e28716b2d9ddb21836d9b27c"
})
Request3 = urllib2.Request(url3,data3)
Res3 = urllib2.urlopen(Request3)
print (Res3.read())



#https://cloud.kingdee.com/passport/signup?from=qy  云之家
