import mysql.connector
mydb = mysql.connector.connect(
  host="localhost", user="root",
  password="root",
  database="datarepresentation"
)

mycursor = mydb.cursor()
sql="CREATE TABLE student(id int auto_increment PRIMARY KEY, name VARCHAR(255), age INT)"
# values = ("Mary","Galway")
mycursor.execute(sql)



#db.commit()