from urllib.request import *
from urllib.error import *
try:
    response = urlopen("https://cuiqingcai.com/index.htm")
except HTTPError as e:
    print(e.reason, e.code, e.headers, sep="\n")
    #
    """
    print(e.reason)
    print(e.code)
    print(e.headers)
    """
"""
输出: 
Not Found
404
Server: nginx/1.10.3 (Ubuntu)
Date: Wed, 05 Sep 2018 13:20:23 GMT
Content-Type: text/html; charset=UTF-8
Transfer-Encoding: chunked
Connection: close
Vary: Cookie
Expires: Wed, 11 Jan 1984 05:00:00 GMT
Cache-Control: no-cache, must-revalidate, max-age=0
Link: <https://cuiqingcai.com/wp-json/>; rel="https://api.w.org/"

"""
# 较好的处理了HTTPError 和URLError , 如果没有异常 就进入else, 打印 request successfully
try:
    response = urlopen("https://www.baidu.com")
except HTTPError as e:
    print(e.reason, e.code, e.headers, sep="\n")
except URLError as e:
    print(e.reason)
else:
    print(response.status)
    print("request successfully")

# 输出: 200 request successfully

# reason 返回的不一定是字符串 也可能是一个对象
import socket
try:
    response = urlopen("https://www.baidu.com", timeout=0.01)
except URLError as e:
    # 判断 e.reason 是不是 socket.timeout 类
    if isinstance(e.reason, socket.timeout):
        print("Time Out")

# 输出: Time Out

