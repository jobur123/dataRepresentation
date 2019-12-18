import mysql.connector
db = mysql.connector.connect(
  host="localhost", user="root",
  password="root", database="datarepresentation"
)
cursor = db.cursor()
sql="insert into student (name, age) values (%s,%s)"
values = ("Mary",21)
cursor.execute(sql, values)

db.commit()
print("One row inserted, ID: ", cursor.lastrowid)