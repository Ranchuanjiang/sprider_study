# csv 读取
import csv
with open("data_04.csv", "r", encoding="utf-8") as cf:
    reader = csv.reader(cf)
    for row in reader:
        print(row)
"""
输出: 
['id name age']
['10001 李四 19']
['10002 王五 20']
['10003 张三 21']
['10004 历史 22']
"""
# 利用pandas.read_csv() 读取 csv 文件

import pandas
df = pandas.read_csv("data_04.csv")
print(df)
"""
输出:
   id name age
0  10001 李四 19
1  10002 王五 20
2  10003 张三 21
3  10004 历史 22
可见用pandas 读取 csv跟佳
"""