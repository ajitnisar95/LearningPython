import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "qdnet",
    password = "zaq123$",
    database = "mypythontestdatabase"
)

mycursor = mydb.cursor(buffered=True)


sql = "SELECT * FROM customers WHERE address LIKE '%Dahisar%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x) 


print("\n Another select query, this time one that prevents sql injection:")

sql = "SELECT * FROM customers WHERE address = %s OR address = %s"
adr = ("Yellow Garden 2", "Dahisar East", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
    print(x) 