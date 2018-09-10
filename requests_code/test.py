# 案例抓取猫眼电影 top100
from requests import *
import re
import json


def get_one_page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
    }
    response = get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    return None


def parse_one_page(text):
    text = text.decode("utf-8")
    pattern = re.compile("<i.*?board-index-.*?>(.*?)</i>")
    pattern1 = re.compile("<img data-src=\"(.*?)\" alt")
    pattern2 = re.compile("<a.*?data-val=.*?>(.*?)</a>")
    pattern3 = re.compile("<p.class=\"star\">(.*?)</p>", re.S)
    pattern4 = re.compile("<p.class=\"re.*?\">(.*?)</p>")
    pattern5 = re.compile("<i class=\"integer\">(.*?)</.*?fraction\">(.*?)</i>")

    result = pattern.findall(text)
    result1 = pattern1.findall(text)
    result2 = pattern2.findall(text)
    result3 = [x.strip() for x in pattern3.findall(text)]
    result4 = pattern4.findall(text)
    result5 = [k+v for k, v in pattern5.findall(text)]
    items =  zip(result, result1, result2, result3, result4, result5)
    for item in items:
        yield {
            "排名:": item[0],
            "封面:": item[1],
            "片面:": item[2],
            "演员表:": item[3],
            "上映时间:": item[4],
            "评分": item[5]
        }

def write_to_file(content):
    with open("猫眼top100.txt", "a", encodeing="utf-8") as f:
        f.write(json.dumps(content, ensure_acsii=False) + "\n")



def main():
    pass

if __name__ == "__main__":
    url = "http://maoyan.com/board/4?offset=0"
    text = get_one_page(url)
    for i in parse_one_page(text):
        print(i)