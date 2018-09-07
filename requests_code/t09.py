# 代理设置
import requests
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "https://10.10.1.10:1080"
}
# 写法
requests.get("https://www.baidu.com", proxies=proxies)
# 若代理需要使用HTTP Basic Auth 可以使用http://user:password@host:post
proxies = {
    "http": "http://user:password@10.10.1.10:3128"
}
requests.get("https://www.baidu.com", proxies=proxies)
# 除了HTTP 代理外, 还支持 SOCKS 协议代理
# 需要安装socks 库
proxies = {
    "http": "sock5://user:password@host:port",
    "https": "sock5//user:password@hosy:port"
}
requests.get("https://www.taobao.com", proxies=proxies)
