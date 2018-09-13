import requests
from bs4 import BeautifulSoup
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
html = requests.get("https://www.taobao.com", headers=headers)
with open("taobao.html", "wb") as f:
    f.write(html.content)

soup = BeautifulSoup(html.content, "lxml") # 可以自动不全更正 html 格式
with open("taobao2.html", "wb") as f:
    # prettify() 方法可以把要解析的字符串 以标准的缩进格式输出
    f.write(soup.prettify().encode("utf-8"))

