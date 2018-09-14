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
    也可以用children 来查看不过是一个生成器类型
    """
    print(soup.p.children)
    for i, child in enumerate(soup.p.children):
        print(i, "---->", child)

    """
    输出:
        0 ----> 
    
    1 ----> <a class="J_MemberPunch h" data-spm="d3" href="//taojinbi.taobao.com/index.htm?auto_take=true">
    <span class="tbh-icon">
    </span>
             领淘金币抵钱
            </a>
    2 ----> 
    
    3 ----> <a class="J_MemberClub h club" href="//vip.taobao.com">
    <span class="tbh-icon">
    </span>
             会员俱乐部
            </a>
    4 ----> 
    
    """
    # 想要查看所有的子孙节点 要用descendants 属性
    for i, child in enumerate(soup.p.descendants):
        print(i, child)
    """
    输出:
    0 
    
    1 <a class="J_MemberPunch h" data-spm="d3" href="//taojinbi.taobao.com/index.htm?auto_take=true">
    <span class="tbh-icon">
    </span>
             领淘金币抵钱
            </a>
    2 
    
    3 <span class="tbh-icon">
    </span>
    4 
    
    5 
             领淘金币抵钱
            
    6 
    
    7 <a class="J_MemberClub h club" href="//vip.taobao.com">
    <span class="tbh-icon">
    </span>
             会员俱乐部
            </a>
    8 
    
    9 <span class="tbh-icon">
    </span>
    10 
    
    11 
             会员俱乐部
            
    12 

    """
    # 父节点 和 祖先节点 用parents 属性
    print(soup.p.a)
    print(list(enumerate(soup.p.a.parents)))
    # 兄弟节点选择 用next_sibling 和 previous_sibling 分别获取下一个和上一个兄弟元素 next_siblings 和 previous_sibings 获取前面的 和后面的兄弟元素

