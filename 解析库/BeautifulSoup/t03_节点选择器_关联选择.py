from bs4 import BeautifulSoup
with open("taobao2.html", "rb") as f:
    soup = BeautifulSoup(f, "lxml")
    # 子节点和子孙节点
    print(soup.p.contents)
    """
    输出:
    ['\n', <a class="J_MemberPunch h" data-spm="d3" href="//taojinbi.taobao.com/index.htm?auto_take=true">
<span class="tbh-icon">
</span>
         领淘金币抵钱
        </a>, '\n', <a class="J_MemberClub h club" href="//vip.taobao.com">
<span class="tbh-icon">
</span>
         会员俱乐部
        </a>, '\n']
    可以看到 所列出来的节点 包含了直接子节点 里面的节点 但是是一块的 想要 在获得子节点里面的子节点 需要用到children
    """
    print(soup.p.children)
    for child in soup.p.children:
        print(child)