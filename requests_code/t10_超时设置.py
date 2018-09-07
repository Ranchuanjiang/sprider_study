# 超时设置
import requests
r = requests.get("http://www.taobao.com", timeout=0.1)
print(r.status_code)
# 输出: 200
# 上面timeout 时间为链接和读取的总时间, 可以单独设置链接和读取时间
# r = requests.get(url, timeout(connect, read, add))
# 分别指定时间 链接, 读取, 总时间
# 想要永久等待 可以不填 或者 设置timeout=None, 默认为None
