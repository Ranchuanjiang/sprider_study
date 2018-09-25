import pymysql
db = pymysql.connect(host="localhost", user="root", password="asd19917300828", port=3306, db="spider1")
cursor = db.cursor()
sql = "CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL , name VARCHAR(255) NOT NULL, age int NOT NULL , PRIMARY KEY (id))"
cursor.execute(sql)
db.close()
