# etree 中 tostring 自动补全
from lxml import etree
text = """
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-2"><a href="link3.html">third item</a></li>
<li class="item-3"><a href="link4.html">fourth item</a></li>
<li class="item-4"><a href="link5.html">fifth item</a>
</ul>
</div>

"""
# 可以看到上面最后一个 标签是有缺失的

html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode("utf-8"))
"""
输出结果:
<html><body><div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-2"><a href="link3.html">third item</a></li>
<li class="item-3"><a href="link4.html">fourth item</a></li>
<li class="item-4"><a href="link5.html">fifth item</a>
</li></ul>
</div>

可以 看到 这个已经被不全了
"""
# 还可以 通过文本文件直接解析
html = etree.parse("test.html", etree.HTMLParser())
result = etree.tostring(html)
print(result.decode("utf-8"))