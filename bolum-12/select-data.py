import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sadikturan_41",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT * FROM products"
sql = "SELECT id,name FROM products"

cursor.execute(sql)

# products = cursor.fetchall()
product = cursor.fetchone()

print(product)
# for p in products:
#     print(p[0], p[1])
