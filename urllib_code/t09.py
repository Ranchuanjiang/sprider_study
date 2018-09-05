from urllib.request import build_opener, HTTPCookieProcessor
import http.cookiejar
filename = "cookie01.txt"
# LWP 格式的 cookie
cookie = http.cookiejar.LWPCookieJar(filename)
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
req = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True,ignore_expires=True)


"""
输出: 参见cookie.txt

"""