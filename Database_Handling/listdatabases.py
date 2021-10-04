import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="qdnet",
    password="zaq123$"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x) 