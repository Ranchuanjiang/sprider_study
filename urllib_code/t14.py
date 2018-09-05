# urlunparse() 接收一个可迭代对象, 但是长度必须为6 否则会抛出 数量过多或者数量不足的问题
from urllib.parse import *
url_data = ["https", "www.baidu.com", "index.html", "user", "a=6", "comment"]
result = urlunparse(url_data)
print(result)

# 输出: https://www.baidu.com/index.html;user?a=6#comment
