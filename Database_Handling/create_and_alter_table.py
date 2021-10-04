import mysql.connector
from mysql.connector import errorcode


mydb = mysql.connector.connect(
    host = "localhost",
    user = "qdnet",
    password = "zaq123$",
)



mycursor = mydb.cursor(buffered=True)



#print("Before Creating:")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x) 

try:
    mycursor.execute("CREATE DATABASE mypythontestdatabase")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("\nDatabase named mypythondatabase already exists.")
    else:
        print(err.msg)
    

#print("\n")
#print("After Creating:")
mycursor.execute("SHOW DATABASES")

print("\n")

mycursor.execute("USE mypythontestdatabase")
try:
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
        print("\nTable named customers already exists in Database named mypythondatabase.")
    else:
        print(err.msg)
    
    
    

print("The tables are:")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)




try:
    mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
except mysql.connector.Error as err:
    print(err.msg)
    print("column id was not created because it most probably already exists.")








print("\n")

print("The rows(data) in customer table are:")
mycursor.execute("select * from customers")

for x in mycursor:
    print(x)

