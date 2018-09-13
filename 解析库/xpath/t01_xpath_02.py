# 节点轴选择
from lxml import etree

html = etree.parse("test.html", etree.HTMLParser())
result = html.xpath("//li[1]/ancestor::*")
print(result)
"""
输出:
[<Element html at 0x240f7667b08>, <Element body at 0x240f7667bc8>, <Element div at 0x240f7667c08>, <Element ul at 0x240f7667c48>]
匹配 第一个li 标签的所有祖先标签节点
"""
result = html.xpath("//li[1]/ancestor::div")
print(result)
"""
输出:[<Element div at 0x1bc094c7c08>]
匹配 第一个li 标签的div 祖先标签节点

"""
result = html.xpath("//li[2]/attribute::*")
print(result)
"""
输出: ['item-1']
匹配第二个li 标签下的所有属性
"""
result = html.xpath("//li/child::a[@href=\"link1.html\"]")
print(result)
"""
输出:[<Element a at 0x2143c548c48>]
匹配所有li 标签下面a子节点 下href 属性为link1.html的 a 标签 节点
"""
result = html.xpath("//li[1]/descendant::*")
print(result)
"""
输出:[<Element a at 0x1e039ca8c48>, <Element span at 0x1e039ca8bc8>]
匹配 第一个li 标签下的所有 子孙标签节点
"""
result = html.xpath("//li[2]/following::*")
print(result)
"""
输出:[<Element li at 0x159ccb08c08>, <Element a at 0x159ccb08c88>, <Element li at 0x159ccb08cc8>, <Element a at 0x159ccb08d08>, <Element li at 0x159ccb08d48>, <Element a at 0x159ccb08dc8>]
匹配第二个li 标签节点后的所有 节点 
"""
result = html.xpath("//li[2]/following::*[2]")
print(result)
"""
输出:[<Element a at 0x17a7b1e8c88>]
输出第二个里标签节点后的第二个标签节点
"""
result = html.xpath("//li[1]/following-sibling::*")
print(result)
"""
输出:[<Element li at 0x1df52808c08>, <Element li at 0x1df52808cc8>, <Element li at 0x1df52808d08>, <Element li at 0x1df52808d48>]
获取当前节点的同级节点
"""
