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
# 父节点
result = html.xpath("//a[@href=\"link4.html\"]/../@class")
print(result)
# 输出: ['item-3']
# 也可以用parent:: 来匹配父节点
result = html.xpath("//a[@href=\"link4.html\"]/parent::*/@class")
print(result)

# 输出结果和上面的一样

# 属性匹配
result = html.xpath("//li[@class=\"item-4\"]")
print(result)
# 结果: [<Element li at 0x2e3b0ad7d08>]

# 文本获取
result = html.xpath("//li[@class=\"item-0\"]/a/text()")
print(result)
# 输出结果: ['first item']
# 另外一种匹配方法
result = html.xpath("//li[@class=\"item-0\"]//text()")
print(result)
# 输出结果: ['first item']
# 属性获取

result = html.xpath("//li/a/@href")
print(result)
# 输出结果:['link1.html', 'link2.html', 'link3.html', 'link4.html', 'link5.html']
# 属性多值匹配 contains() 函数
text = """
<div>
    <ul>
        <li class="li list_item" name="lisa"><a href="link1.html">first item</a></li>
        <li class="li list_item" ><a href="link2.html">second item</a></li>
    </ul>
<div>
"""
html = etree.HTML(text)
# result = html.xpath("//li[@class li]/a/text()")   # 报错!
result = html.xpath("//li[contains(@class, \"li\")]/a/text()")
print(result)
# 输出结果: ['first item', 'second item']

result = html.xpath("//li[contains(@class, \"li\") and @name=\"lisa\"]/a/text()")
print(result)
# 输出结果: ['first item']
html = etree.parse("test.html", etree.HTMLParser())
result = html.xpath("//li[1]/a/text()")
print(result)
result = html.xpath("//li[last()]/a/text()")
print(result)
result = html.xpath("//li[position()<3]/a/text()")
print(result)
result = html.xpath("//li[last()-1]/a/text()")
print(result)
"""
输出结果:
['first item']
['fifth item']
['first item', 'second item']
['fourth item']

"""
