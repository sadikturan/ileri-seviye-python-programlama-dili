import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sadikturan_41",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT name,categoryid FROM products"
# sql = "SELECT name FROM categories"
# sql = "SELECT products.name,categories.name from products inner join categories on products.categoryid=categories.id"
# sql = "SELECT p.name,c.name from products p inner join categories c on p.categoryid=c.id"
sql = "SELECT p.name,c.name from products p inner join categories c on p.categoryid=c.id WHERE c.name='Bilgisayar'"

cursor.execute(sql)

result = cursor.fetchall()

print(result)
