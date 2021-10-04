import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "qdnet",
    password = "zaq123$",
    database = "mypythontestdatabase"
)

mycursor = mydb.cursor(buffered=True)

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected") 