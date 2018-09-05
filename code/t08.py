from urllib.request import build_opener, HTTPCookieProcessor
import http.cookiejar
filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
req = opener.open("http://www.baidu.com")
cookie.save()
