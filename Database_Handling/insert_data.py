import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "qdnet",
    password = "zaq123$",
    database = "mypythontestdatabase"
)

mycursor = mydb.cursor(buffered=True)

try:
    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val1 = ("John", "Highway 21")
    val2 = ("Ajit","Dahisar East")
    mycursor.execute(sql, val1)
    mycursor.execute(sql,val2)
except mysql.connector.Error as err:
    print(err.msg)

try:
    mydb.commit()
except mysql.connector.Error as err:
    print(err.msg)

print(mycursor.rowcount, "records inserted.")