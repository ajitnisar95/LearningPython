import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "qdnet",
    password = "zaq123$",
    database = "mypythontestdatabase"
)

mycursor = mydb.cursor(buffered=True)


mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


