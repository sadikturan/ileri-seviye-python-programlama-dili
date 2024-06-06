import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sadikturan_41",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT COUNT(*) FROM products"
# sql = "SELECT AVG(Price) FROM products"
# sql = "SELECT SUM(Price) FROM products"
# sql = "SELECT MIN(Price) FROM products"
# sql = "SELECT MAX(Price) FROM products"
# sql = "SELECT name,price FROM products WHERE Price = (SELECT MAX(Price) FROM products)"
sql = "SELECT name,price FROM products ORDER BY price DESC LIMIT 1" 

cursor.execute(sql)

result = cursor.fetchall()

print(result)
