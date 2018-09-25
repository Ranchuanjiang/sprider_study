import pymysql
id = "20100001"
name = "Bob"
age = 20
db = pymysql.connect(host="localhost", user="root", password="asd19917300828", db="spider1")
cursor = db.cursor()
sql = "INSERT INTO students(id , name, age ) VALUES(%s ,%s ,%s)"
try:
    cursor.execute(sql, (id, name, age))
    db.commit()
except:
    db.rollback()
db.close()
"""
通用 sql 插入数据
以字典的方式传入数据
如下:
data = {
    "id" : "20100001",
    "user": "Bob"
    "age": 20
}
table = "students"
keys = ", ".join(data.keys())
values = ", ".join(["%s"]*len(data))
sql = "INSERT INTO {0}({}) VALUES({})".format(table, keys, values)
"""