import urllib.request
response = urllib.request.urlopen("http://httpbin.org")
# print(response.read().decode("utf-8"))
print(type(response))
# 获得状态码
print(response.status)
# 获得响应头
for i in response.getheaders():
    print(i[0], " : ", i[1])
# 获得服务器信息
