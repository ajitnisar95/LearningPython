import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="qdnet",
    password="zaq123$"
)

mycursor = mydb.cursor()
#print("\n")
print("Before Creating:")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x) 


mycursor.execute("CREATE DATABASE mypythontestdatabase")
print("\n")
print("After Creating:")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x) 



mycursor.execute("DROP DATABASE mypythontestdatabase")
print("\n")
print("After Deleting:")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x) 


