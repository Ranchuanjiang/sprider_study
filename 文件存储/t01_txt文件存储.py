# txt 文件存储
import requests
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
import re
url = "https://www.zhihu.com/explore"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36"
}
html = requests.get(url, headers=headers)
"""
soup = BeautifulSoup(html.text, "lxml")

questions = soup.find_all(name="div", attrs={"class": "explore-feed feed-item"} )
for q in  questions:

    question = q.h2.string
    a = q.find_all(name="a", attrs="author-link")
    for i in a:
        author = i.string
    ans = q.find_all(name="textarea")
    for i in ans:

        j =[k.replace("<br>", "") for k in re.findall("<.*?>(.*?)</.*?>", i.string)]
        answer = "\n".join(j)
    with open("zhihu.txt", "a", encoding="utf-8") as file:
        file.write(question)
        file.write(author)
        file.write(answer)
"""
doc = pq(html.text)
items = doc(".explore-tab .feed-item").items()
for item in items:
    question = item.find("h2").text()
    author = item.find(".author-link-line").text()
    answer = pq(item.find(".content").html()).text()
    file = open("zhihu.txt", "a", encoding="utf-8")
    file.write("\n".join([question, author, answer]).strip())
    file.write("\n" + "#"*50 + "\n")
    file.close()

