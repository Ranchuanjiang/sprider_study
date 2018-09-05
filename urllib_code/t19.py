# 分析 Robots 协议
from urllib.robotparser import *
from urllib.request import *
url = "http://www.jianshu.com/robots.txt"
req = Request(url)
req.add_header("User-Agent", " Mozilla/5.0 (Windows NT 10.0; Win64; x64)")
print(urlopen(req).read().decode("utf-8"))
# 创建一个RobotFileParser 对象

rp = RobotFileParser()
# 指定 robots 协议地址
# 还可以直接在创建的时候指定
# rp = RobotFileParser(url)
rp.set_url(url)
rp2 = RobotFileParser()
rp2.parse(urlopen(req).read().decode("utf-8").split("\n"))

# 必须有read() 不调用这个方法 下面判定都会为False, 该方法不返回内容, 只执行读取操作
rp.read()

print(rp.can_fetch("*", "https://www.jianshu.com/p/6c80df0c0280"))
print(rp.can_fetch("*", "https://www.jianshu.com/search?q=python&page=1&type=collections"))
print(rp2.can_fetch("*", "https://www.jianshu.com/p/6c80df0c0280"))
print(rp2.can_fetch("*", "https://www.jianshu.com/search?q=python&page=1&type=collections"))

"""
输出: 
# See http://www.robotstxt.org/wc/norobots.html for documentation on how to use the robots.txt file
#
# To ban all spiders from the entire site uncomment the next two lines:
User-agent: *
Disallow: /search
Disallow: /convos/
Disallow: /notes/
Disallow: /admin/
Disallow: /adm/
Disallow: /p/0826cf4692f9
Disallow: /p/d8b31d20a867
Disallow: /collections/*/recommended_authors
Disallow: /trial/*
Disallow: /keyword_notes
Disallow: /stats-2017/*

User-agent: trendkite-akashic-crawler
Request-rate: 1/2 # load 1 page per 2 seconds
Crawl-delay: 60

User-agent: YisouSpider
Request-rate: 1/10 # load 1 page per 10 seconds
Crawl-delay: 60

User-agent: Cliqzbot
Disallow: /

User-agent: Googlebot
Request-rate: 2/1 # load 2 page per 1 seconds
Crawl-delay: 10

False   <---- 为什么为False
False 
True
False
"""
