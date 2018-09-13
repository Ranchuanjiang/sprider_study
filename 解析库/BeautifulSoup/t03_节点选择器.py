from bs4 import BeautifulSoup
with open("taobao2.html", "rb") as f:

    soup = BeautifulSoup(f, "lxml")
    # string 获得节点元素包含的文本内容
    print(soup.title.string)
    print(type(soup.title))
    """
    输出:
       淘宝网 - 淘！我喜欢
    <class 'bs4.element.Tag'>
    """
    print(soup.p)
    """
    输出:
    <p class="member-tjb">
    <a class="J_MemberPunch h" data-spm="d3" href="//taojinbi.taobao.com/index.htm?auto_take=true">
    <span class="tbh-icon">
    </span>
             领淘金币抵钱
      
    """
    # 属性选择
    print(soup.p.attrs)
    print(soup.p.attrs["class"])
    # 输出: {'class': ['member-tjb']}
    # 输出: ['member-tjb']
    print(soup.p["class"])
    # 输出: ['member-tjb']
    # 注意: 有时候某属性输出是str 类型 有时是列表 如果 属性值是唯一的就是输出str 类型, 如果属性值有多个就是列表类型
    # 嵌套选择
    print(soup.head.title)
    """
    输出:
    <title>
   淘宝网 - 淘！我喜欢
  </title>
    """
    print(soup.head.title.string)
    # 输出:  淘宝网 - 淘！我喜欢
