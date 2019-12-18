import mysql.connector
db = mysql.connector.connect(
  host="localhost", user="root",
  password="root"
)

cursor = db.cursor()
# sql="insert into student (name, address) values (%s,%s)"
# values = ("Mary","Galway")
cursor.execute("CREATE DATABASE datarepresentation")



#db.commit()