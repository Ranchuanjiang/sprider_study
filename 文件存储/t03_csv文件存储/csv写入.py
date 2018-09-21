# csv 写入
import csv
with open("data.csv", "w", encoding="utf-8") as cf:
    writer = csv.writer(cf)
    writer.writerow(["id", "name", "age"])
    writer.writerow(["01", "李四", "19"])
    writer.writerow(["02", "王五", "20"])
    writer.writerow(["03", "张三", "21"])

"""
输出:
id,name,age

01,李四,19

02,王五,20

03,张三,21
默认以逗号分隔
此时 可以看见中间有一行空格 此时 需要使用newline="" , 案例如下
"""
with open("data_01.csv", "w", newline="", encoding="utf-8") as cf:
    writer = csv.writer(cf)
    writer.writerow(["id", "name", "age"])
    writer.writerow(["01", "李四", "19"])
    writer.writerow(["02", "王五", "20"])
    writer.writerow(["03", "张三", "21"])

# 此时就没有空行了
# 更改默认分隔符 需要使用 delimiter参数
with open("data_02.csv", "w", newline="", encoding="utf-8") as cf:
    writer = csv.writer(cf, delimiter=" ")
    writer.writerow(["id", "name", "age"])
    writer.writerow(["01", "李四", "19"])
    writer.writerow(["02", "王五", "20"])
    writer.writerow(["03", "张三", "21"])
"""
输出:
id name age
01 李四 19
02 王五 20
03 张三 21

"""

# 可以使用 writerows() 写入多行
with open("data_03.csv", "w", newline="", encoding="utf-8") as cf:
    writer = csv.writer(cf, delimiter=" ")
    writer.writerow(["id", "name", "age"])
    writer.writerows([["01", "李四", "19"], ["02", "王五", "20"], ["03", "张三", "21"]])

# 输出同上

# 用字典的方式写入
with open("data_04.csv", "w", newline="", encoding="utf-8") as cf:
    fn = ["id", "name", "age"]
    writer = csv.DictWriter(cf, fieldnames=fn, delimiter=" ")
    writer.writeheader()
    writer.writerows([
        {"id": 10001, "name": "李四", "age": 19},
        {"id": 10002, "name": "王五", "age": 20},
        {"id": 10003, "name": "张三", "age": 21}
    ])
"""
输出:
id name age
10001 李四 19
10002 王五 20
10003 张三 21
"""
# 如果要追加元素需要 将w 改为a 此时不需要调用 writeheader()

with open("data_04.csv", "a", newline="", encoding="utf-8") as cf:
    fn = ["id", "name", "age"]
    writer = csv.DictWriter(cf, fieldnames=fn, delimiter=" ")
    writer.writerows([
        {"id": 10004, "name": "历史", "age": 22},
    ])
