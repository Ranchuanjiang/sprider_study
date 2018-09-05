# urllib 中的 parse 模块, 定义了处理url的标准接口, 实现对url 的各部分抽取, 合并,以及连接的替换
from urllib.parse import urlparse
result = urlparse("https://www.baidu.com/index.html;user?id=5#comment")
print(type(result), result, sep="\n")

"""
输出:
<class 'urllib.parse.ParseResult'>
ParseResult(scheme='https', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
可以发现 urlparse 将 url 拆分为了 六部分:
1. scheme: 代表协议
2. netloc: 代表域名
3. path: 代表访问路径
4. params: 代表参数
5. query: 查询条件, 一般用作GET 类型的url
6. fragment: 锚点
即: scheme://netloc/path;params?query#fragment
"""
#  urlparse() 的其他配置
# urlparse(urlstring, scheme="", )allow_fragments=True)
# urlstring : 必填 待解析的url
# scheme 默认协议(http, https 等)
result = urlparse("www.baidu.com/index.html;user?id=5#comment", scheme="https")
print(result)
"""
输出: 
ParseResult(scheme='https', netloc='', path='www.baidu.com/index.html', params='user', query='id=5', fragment='comment')

"""
# url带上 scheme
result = urlparse("http://www.baidu.com/index.html;user?id=5#comment",  scheme="https")
print(result)
"""
输出: 
ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
此时当url 里面有 scheme 参数 时 使用的时url 里面的scheme 参数 外部设置的不起作用了
"""
# allow_fragments 这是设置是否忽略 fragment  如果时False 就是忽略,只解析其他部分 fragment 会被忽略
result = urlparse("http://www.baidu.com/index.html;user?id=5#comment", allow_fragments=False)
print(result)

"""
输出: 
ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5#comment', fragment='')
此时fragment为空 但是 我们发现 原本应该在fragment里的 到了quer 里面去了
"""
# 假设 url 里面没有 params 和 query

result = urlparse("http://www.baidu.com/index.html#comment", allow_fragments=False)
print(result)

"""
输出:
ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html#comment', params='', query='', fragment='')
如果url 里面没有params 和query 那么 fragment 就会变成 path 里的一部分
"""

# 返回ParseResult 其实是一个元组
result = urlparse("http://www.baidu.com/index.html#comment", allow_fragments=False)
print(result.scheme, result[0], result.netloc, result[1], sep="\n")
print(result.path, result[2], sep="\n")
"""
输出:
http
http
www.baidu.com
www.baidu.com
/index.html#comment
/index.html#comment
可以发现两种 方法获得的数据是一样的都可以获得数据
"""