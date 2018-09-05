from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError
# 代理 使用ProxyHandler 构建
proxy_handler = {
    "http": "http://127.0.0.0:9743",
    "https": "https://127.0.0.0;9743"
}
p = ProxyHandler(proxy_handler)
opener = build_opener(p)

try:
    rep = opener.open("http://www.baidu.com")
    print(re.read().decode("utf-8"))
except URLError as e:
    print(e.reason)
p