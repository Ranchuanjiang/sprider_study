from bs4 import BeautifulSoup
with open("taobao2.html", "rb") as f:

    soup = BeautifulSoup(f, "lxml")
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
            </a>
    <a class="J_MemberClub h club" href="//vip.taobao.com">
    <span class="tbh-icon">
    </span>
             会员俱乐部
            </a>
    </p>
    可以出 此时将网页中的p 节点打印出来了
    注意: 此种选择 只打印第一个匹配到的结果
    """

