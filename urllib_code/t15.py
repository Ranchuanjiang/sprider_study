# urlsplit() 此方法和 urlparse() 很相似, 不过只返回5 个结果, urlparse() 里面的params 这一部分会加到path里面

from urllib.parse import urlsplit
result = urlsplit("https://www.baidu.com/index.html;user?a=6#comment")
print(type(result), result, sep="\n")

"""
输出:
<class 'urllib.parse.SplitResult'>
SplitResult(scheme='https', netloc='www.baidu.com', path='/index.html;user', query='a=6', fragment='comment')
"""

# 返回的类型式SplitResult 也是一个元组类型
print(result.scheme, result[0])

# 输出: https https

# urlunsplit() 和 urlunsparse() 类似, 区别就是长度必须为 5

from urllib.parse import urlunsplit

url_data = ["https", "www.baidu.com", "index.html;user", "a=6", "comment"]
result = urlunsplit(url_data)
print(result)

"""
输出:
https://www.baidu.com/index.html;user?a=6#comment
"""
