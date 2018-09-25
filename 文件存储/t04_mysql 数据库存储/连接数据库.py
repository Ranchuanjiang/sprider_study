# 链接数据库
import pymysql
db = pymysql.connect(host="localhost", user="root", password="asd19917300828", port=3306)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version:", data)
cursor.execute("create DATABASE spider1 DEFAULT CHARACTER SET utf8mb4")
db.close()