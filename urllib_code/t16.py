"""
urljoin() 生成新链接的另外一个方法, 提供一个base_url(基础链),作为第一参数, 将新的连接做为第二个参数
该方法会分析base_url 的scheme, 和 netloc, path 这三个内容并对新链接进行补充最后返回结果

"""
from urllib.parse import *
print(urljoin("http://www.baidu.com", "FAQ.html"))
print(urljoin("http://www.baidu.com", "https://cuiqingcai.com/FAQ.html"))
print(urljoin("http://www.baidu.com/about.html", "https://cuiqingcai.com/FAQ.html"))
print(urljoin("http://www.baidu.com/about.html", "https://cuiqingcai.com/FAQ.html?quest=2"))
print(urljoin("http://www.baidu.com?wd=abc", "https://cuiqingcai.com/index.html"))
print(urljoin("www.baidu.com", "?category=2#comment"))
print(urljoin("www.baidu.com#comment", "?category=2"))

"""
输出:
http://www.baidu.com/FAQ.html
https://cuiqingcai.com/FAQ.html
https://cuiqingcai.com/FAQ.html
https://cuiqingcai.com/FAQ.html?quest=2
https://cuiqingcai.com/index.html
www.baidu.com?category=2#comment
www.baidu.com?category=2
可以看到 base_url 提供三项 scheme path netloc 如果这三项新的链接不存在就给予补充, 如果新连接存在就使用 新链接的部分
并且 base_url 里面的 params query, fragment 是不起作用的
"""