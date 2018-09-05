# 发送登陆信息
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.request import URLError, Request, urlopen

username = "username"
password = "password"
url = "http://localhost:5000/"

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)

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
