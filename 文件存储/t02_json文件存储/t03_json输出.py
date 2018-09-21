# json 输出
import json

data = [
    {
        "name": "Bob",
        "gender": "male",
        "birthday": "1991-1-1"
    }
]

with open("DATA_1.json", "w") as f:
    f.write(json.dumps(data, indent=2))
"""
注意文件名大小写不敏感
indent=2 表示写入时 代表缩进字符格式如果不写输入就是一行 没有缩进 
"""
# 输出中文呢
data = [
    {
        "name": "李四",
        "gender": "男",
        "birthday": "1991-1-1"
    }
]
with open("DATA_2.json", "w") as f:
    f.write(json.dumps(data, indent=2))

"""
输出:
[
  {
    "name": "\u674e\u56db",
    "gender": "\u7537",
    "birthday": "1991-1-1"
  }
]
可以看见中文都变成了unicode字符
此时还需要 制定参数 ensure_ascii 为False

"""
data = [
    {
        "name": "李四",
        "gender": "男",
        "birthday": "1991-1-1"
    }
]
with open("DATA_3.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(data, indent=2, ensure_ascii=False))

# 此时 输出json 文本内容就变成了 中文

