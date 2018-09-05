# urlencode() 在构造 GET请求参数的时候非常有用
from urllib.parse import *
params = {
    "name": "germey",
    "age": 18
}
base_url = "http://www.baidu.com?"
url = base_url + urlencode(params)
print(url)

# 输出: http://www.baidu.com?name=germey&age=18
# parse_qs() 反序列化

query = "name=germey&age=18"
print(parse_qs(query))

# 输出: {'name': ['germey'], 'age': ['18']}

# parse_qsl() 同样反序列化输出, 不过输出的是元组列表

query = "name=germey&age=18"
print(parse_qsl(query))

# 输出结果: [('name', 'germey'), ('age', '18')]