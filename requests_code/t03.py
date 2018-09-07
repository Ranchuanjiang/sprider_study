# 抓取网页
# 知乎 发现界面

import requests
import re
# 如果不添加 header 信息  就不能正常请求  header 也可以添加其他字段的信息
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}

r = requests.get("https://www.zhihu.com/explore", headers=header)
pattern = re.compile("explore-feed.*?question_link.*?>(.*?)</a>", re.S)
titles = re.findall(pattern, r.text)
# print(r.text)
# titles 是正则表达式所返回的类型 属于列表
for i in titles:
    print(i.strip())
"""
输出:
如何评价秦皇岛海港区超市杀人案告破：嫌疑人杀死两人后畏罪自杀？
如何评价主题医院精神续作《双点医院》？
有什么排骨的好吃做法？排骨怎么做才不柴？
如何看待 13 岁男孩深夜玩「吃鸡」手游后坠楼身亡？
中科大郭光灿团队研制出「完全可控量子模拟器」，完成了怎样的突破，对推进量子计算机的研制有何意义？
如何看待807黄其淋和敖子逸、陈泗旭的会面？
魏璎珞爱皇上还是傅恒?
有哪些生物学上的事实，没有一定生物学知识的人不会相信？
无效行为被撤销有什么意义？
普通人是否需要补钙？为什么？

"""
# 抓取二进制数据
# 图片, 音频, 视频 本质上是以二进制 码组成的
r1 = requests.get("https://github.com/favicon.ico")
# print(r1.text)
# print(r1.content)
"""
输出:
第一排为乱码
第二排输出为b 开头代表bytes 类型的数据 以str 表现

"""
# 保存文件
with open("favicon.ico", "wb") as  fa:
    fa.write(r1.content)
# 此时完成了图片的抓取 同理音频 和 视频文件也可以以这种方式抓取

