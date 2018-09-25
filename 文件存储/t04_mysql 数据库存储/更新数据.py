import pymysql

db = pymysql.connect(host="localhost", user="root", password="asd19917300828", db="spider1")
cursor = db.cursor()
"""
sql = "UPDATE students SET age = %s WHERE name = %s"
try:
    cursor.execute(sql, (25, "Bob"))
    db.commit()
except:
    db.rollback()
db.close()
"""
# 实现 如果数据存在就更新数据如果数据不存在就插入数据
data = {
    "id": "20100001",
    "name": "Bob",
    "age": 28
}
table = "students"
keys = ", ".join(data.keys())
values = ", ".join(["%s"]*len(data))
sql = "INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE".format(table=table, keys=keys, values=values)
update = ", ".join(["{key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print("Successful")
        db.commit()
except:

    print("Failed")
    db.rollback()

db.close()