# quote() 该方法可以将内容转化为URL编码格式,url 带中文参数的时候,又是会乱码,此时用这个方法可以将中文字符转化为url 编码
from urllib.parse import *
keyword = "花瓶"
url = "https://www.baidu.com/s?wd=" + quote(keyword)
print(url)

# 输出: https://www.baidu.com/s?wd=%E8%8A%B1%E7%93%B6

# 同样 有quote() 就有unquote() 方法

url = "https://www.baidu.com/s?wd=%E8%8A%B1%E7%93%B6"
print(unquote(url))

# 输出: https://www.baidu.com/s?wd=花瓶