# 发送登陆信息
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.request import URLError, Request, urlopen

username = "username"
password = "password"
url = "http://localhost:5000/"
# 创建一个密码管理对象，用来保存 HTTP 请求相关的用户名和密码.
p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)
# HTTPBasicAuthHandler 管理认证
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)


try:
    '''
    result = opener.open(url)
    html = result.read().decode("utf-8")
    print(html)
    '''
    response = urlopen(url)
    print(response.read().decode("utf-8"))

except URLError as e:
    print(e.reason)
