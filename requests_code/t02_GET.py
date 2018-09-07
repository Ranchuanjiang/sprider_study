2# GET 请求
import requests

r = requests.get("http://httpbin.org/get")
print(r.text)

"""
输出:
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.19.1"
  }, 
  "origin": "183.230.138.173", 
  "url": "http://httpbin.org/get"
}
"""

# 需要传递一些数据 加入name = germey age = 18
data = {
    "name": "germey",
    "age": 18
}
r1 = requests.get("http://httpbin.org/get", params=data)
print(r1.text)
print(type(r1.text))
"""
输出:
{
  "args": {
    "age": "18", 
    "name": "germey"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Accept-Encoding": "gzip, deflate", 
    "Connection": "close", 
    "Host": "httpbin.org", 
    "User-Agent": "python-requests/2.19.1"
  }, 
  "origin": "183.230.138.173", 
  "url": "http://httpbin.org/get?name=germey&age=18"
}
<class 'str'>
可以发现此时的 连接变成了: http://httpbin.org/get?name=germey&age=18
也可以在给定请求的时候直接将url 设置为 上面这个地址
"""
# 不过网页返回结果类型其实是str 字符串类型的, 但是实际是json格式的 这里就可以调用json() 来解析并返回字典类型

r3 = requests.get("http://httpbin.org/get?name=germey&age=18")
print(r3.json())
print(type(r3.json()))
"""
输出:
<class 'str'>
{'args': {'age': '18', 'name': 'germey'},
 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 
 'Connection': 'close', 'Host': 'httpbin.org', 
 'User-Agent': 'python-requests/2.19.1'}, 
 'origin': '183.230.138.173',
  'url': 'http://httpbin.org/get?name=germey&age=18'
  }
<class 'dict'>

"""