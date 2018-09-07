# 会话维持
import requests
# 设置cookies 检查是否有
requests.get("http://httpbin.org/cookies/set/number/1234567890")
r = requests.get("http://httpbin.org/cookies")
print(r.text)
"""
输出:
{
  "cookies": {}
}
此时并没有cookies
"""
# 使用Session
s = requests.Session()
s.get("http://httpbin.org/cookies/set/number/1234567890")
r = s.get("http://httpbin.org/cookies")
print(r.text)
"""
输出:
{
  "cookies": {
    "number": "1234567890"
  }
}
此时可以看见: 在cookies 里面保留了 number 信息

"""