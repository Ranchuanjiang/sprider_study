# timeout
import urllib.request
''''
超时

response = urllib.request.urlopen("http://httpbin.org/get", timeout=0.1)
print(response.read())

'''

# 加入socket模块
# 捕获异常
import socket
import urllib.error
try:
    response = urllib.request.urlopen(" http://httpbin.org/get", timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print("TIME OUT")
