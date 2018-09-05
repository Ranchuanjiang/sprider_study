from urllib.request import *
import http.cookiejar
cookie = http.cookiejar.LWPCookieJar()
# 用load() 方法调用本地的cookie文件
cookie.load("cookie01.txt", ignore_discard=True, ignore_expires=True)
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
response = opener.open("http://www.baidu.com")
print(response.read().decode("utf-8"))


"""
输出: 百度网页源代码

"""
