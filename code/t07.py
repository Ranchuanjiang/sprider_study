# 处理cookie
from urllib.request import HTTPCookieProcessor, build_opener, Request, urlopen
import http.cookiejar

cookie = http.cookiejar.CookieJar()

handler = HTTPCookieProcessor(cookie)
opener = build_opener(handler)
req = Request("http://www.baidu.com")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
result = opener.open(req)
print(result.getheadlers())
# print(type(cookie))
for item in cookie:
    print(item.name, ": ",  item.value)

