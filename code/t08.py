from urllib.request import build_opener, HTTPCookieProcessor
import http.cookiejar
# 生成cookie 文件
filename = "cookie.txt"
# 将文件保存为Mozilla 类型浏览器的 cookie 格式 文件
# 申明一个 cookie 对象
cookie = http.cookiejar.MozillaCookieJar(filename)
# 用HTTPCookieProcessor 构建handler
handler = HTTPCookieProcessor(cookie)
# 用build_opener 构建一个opener
opener = build_opener(handler)
req = opener.open("http://www.baidu.com")
# 保存cookie
cookie.save(ignore_discard=True, ignore_expires=True)


"""
输出: 参见cookie.txt

"""
