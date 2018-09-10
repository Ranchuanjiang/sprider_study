# 获取所有节点
from lxml import etree
html = etree.parse("test.html", etree.HTMLParser())

# * 代表所有节点

result = html.xpath("//*")
print(result)

"""
输出:
[<Element html at 0x21f05286f08>, <Element body at 0x21f052a4048>, <Element div at 0x21f052a4088>, <Element ul at 0x21f052a40c8>, <Element li at 0x21f052a4108>, <Element a at 0x21f052a4188>, <Element li at 0x21f052a41c8>, <Element a at 0x21f052a4208>, <Element li at 0x21f052a4248>, <Element a at 0x21f052a4148>, <Element li at 0x21f052a4288>, <Element a at 0x21f052a42c8>, <Element li at 0x21f052a4308>, <Element a at 0x21f052a4348>]

"""
# 匹配指定节点

result = html.xpath("//li")
print(result)
"""
输出:
[<Element li at 0x1ed0de14108>, <Element li at 0x1ed0de141c8>, <Element li at 0x1ed0de14248>, <Element li at 0x1ed0de14288>, <Element li at 0x1ed0de14308>]

"""
# 子节点 用/
result = html.xpath("//li/a")
print(result)
"""
输出:
[<Element a at 0x1d036e24048>, <Element a at 0x1d036e24088>, <Element a at 0x1d036e240c8>, <Element a at 0x1d036e24188>, <Element a at 0x1d036e24208>]
"""
# 子孙节点//
result = html.xpath("//li//a")
print(result)
"""
输出:
[<Element a at 0x1d036e24048>, <Element a at 0x1d036e24088>, <Element a at 0x1d036e240c8>, <Element a at 0x1d036e24188>, <Element a at 0x1d036e24208>]
"""
# 检测子节点/
result = html.xpath("//ul/a")
print(result)
# 输出为: []
# 子孙节点可以 匹配
result = html.xpath("//ul//a")
print(result)
"""
输出:
[<Element a at 0x250e3403048>, <Element a at 0x250e3403088>, <Element a at 0x250e34030c8>, <Element a at 0x250e3403108>, <Element a at 0x250e3403148>]
"""