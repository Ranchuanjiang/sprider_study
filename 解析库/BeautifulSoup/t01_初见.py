"""
解析器:
python 标准库: BeautifulSoup(markup, "html.parser") python内置标准库 速度适中 劣势: python2.7.3 及3.2.2之前的版本文档容错差
lxml HTML 解析器: BeautifulSoup(markup, "lxml") 速度快 容错能力强 劣势: 需要安装语言库
lxml xml 解析器: BeautifulSoup(markup, "xml") 速度快, 唯一支持xml 的解析器 劣势: 需要安装c语言库
html5lib BeautifulSoup(markup, "html5lib") 最好的容错性, 以浏览器的方式解析文档, 生成html5 格式文档, 劣势: 速度慢. 不依赖 外部扩展
"""

# 用lxml解析器 来解析网页 容错率高速度快

from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>hello world</p>", "lxml")
print(soup.p.string)
# 输出: hello world
