import requests

# POST 请求

data = {"name": "gremey", "age": 18}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)

"""
输出:
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "age": "18", 
    "name": "gremey"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Content-Length": "18", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.19.1"
  }, 
  "json": null, 
  "origin": "183.230.138.173", 
  "url": "http://httpbin.org/post"
}
此时 传输的数据在from 里面 表示POST 请求成功
"""
# 响应
r1 = requests.get("https://www.baidu.com")
print(type(r1.status_code), r1.status_code)
print(type(r1.headers), r1.headers)
print(type(r1.cookies), r1.cookies)
print(type(r1.url), r1.url)
print(type(r1.history), r1.history)
"""
输出:
<class 'int'> 200
<class 'requests.structures.CaseInsensitiveDict'> {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'Keep-Alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Fri, 07 Sep 2018 04:56:56 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:24:32 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
<class 'requests.cookies.RequestsCookieJar'> <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
<class 'str'> https://www.baidu.com/
<class 'list'> []
"""
r3 = requests.get("https://www.jianshu.com")
if r3.status_code == requests.codes.forbidden:
    print("访问被服务器禁止了!")
else:
    print(r3.status_code)
