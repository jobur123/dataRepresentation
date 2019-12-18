import mysql.connector
db = mysql.connector.connect(
  host="localhost", user="root",
  password="root", database="datarepresentation"
)
cursor = db.cursor()
sql="SELECT * from student where id = %s"
values = (1,)
cursor.execute(sql, values)
result = cursor.fetchall()
for x in result:
  print(x)
#print("One row inserted, ID: ", cursor.lastrowid)