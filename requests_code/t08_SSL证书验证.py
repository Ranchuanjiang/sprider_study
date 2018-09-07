# SSL 证书验证
import requests
# r = requests.get("https://www.12306.cn")
r = requests.get("https://www.12306.cn", verify=False)
print(r.status_code)
# 出现了 SSLError
# 此时需要设置verify 参数 为False 默认为True, verify是控制是否检查证书的
# 设置后返回状态码 200 表示请求成功, 可是 还是有一个警告信息
# 通过捕获日志警告信息 忽略

import logging
logging.captureWarnings(True)
r1 = requests.get("https://www.12306.cn", verify=False)
print(r1.status_code)

# 不过还可以 通过制定本地的证书用作 客户端证书, 可以是单文件, 也可以是包含证书 和密钥的 路径的元组
# R = requests.get(url, cert=("/path/sever.crt", "/path/key"))