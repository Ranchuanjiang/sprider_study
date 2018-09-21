# 读取json 文件
import json

# 使用loads() 方法将json 文本字符串转化为json 对象 可以用过dumps() 方法将json 对象转化为文本字符串

strJson = """[
    {
        "name": "Bob",
        "gender": "male",
        "birthday": "1991-1-1"
    },
    {
        "name": "Selina",
        "gender": "female",
        "birthday": "1995-1-1"
    }
]"""
print(type(strJson))
data = json.loads(strJson)
print(data)
print(type(data))

"""
输出:
<class 'str'>
[{'name': 'Bob', 'gender': 'male', 'birthday': '1991-1-1'}, {'name': 'Selina', 'gender': 'female', 'birthday': '1995-1-1'}]
<class 'list'>
由于最外层是中括号所以 最终类型是列表
"""
print(data[0]["name"])
print(data[0].get("name"))
print(data[0].get("age"))
print(data[0].get("age", 18))
"""
输出: 
Bob
Bob
None
18
通过get()获取到的值 如果 传入的键没有找到 会返回None, 此时可以通过传入 第二个参数 作为未找到值后返回的默认值
"""
# 注意 json 数据需要使用双引号包裹 不然会报错
StrJson = """[
    {
        'name': 'Bob',
        'gender': 'male',
        'birthday': '1991-1-1'
    }]"""
# Data = json.loads(StrJson)
# print(Data)
# 报错内容: json.decoder.JSONDecodeError: Expecting property name enclosed in double quotes: line 3 column 9 (char 16)

# 从文本中读取json 数据需要先读取
with open("data.json", "r") as f:
    s_Json = f.read()
    j_data = json.loads(s_Json)
    print(j_data)

"""
输出:
[{'name': 'Bob', 'gender': 'male', 'birthday': '1991-1-1'}, 
{'name': 'Selina', 'gender': 'female', 'birthday': '1995-1-1'}
]
 """

