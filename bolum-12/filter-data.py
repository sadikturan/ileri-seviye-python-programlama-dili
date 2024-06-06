import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sadikturan_41",
    database = "shopdb"
)

cursor = db.cursor()

# sql = "SELECT * from products WHERE id=1"
# sql = "SELECT * from products WHERE id>=1"
# sql = "SELECT * from products WHERE name='Samsung S25'"
# sql = "SELECT * from products WHERE name='Samsung S25' and price=50000"
# sql = "SELECT * from products WHERE name='Samsung S25' or price=50000"
# sql = "SELECT * from products WHERE name='Samsung S25' or price=50000"
# sql = "SELECT * from products WHERE name='Samsung S25' or price=50000"
# sql = "SELECT * from products WHERE name LIKE '%Samsung%'"
# sql = "SELECT * from products WHERE name LIKE 'Samsung%'"
# sql = "SELECT * from products WHERE name LIKE '%Samsung'"
sql = "SELECT * from products WHERE name LIKE '%Samsung%' or description LIKE '%iyi%'"

cursor.execute(sql)

# result = cursor.fetchone()
result = cursor.fetchall()

def getProductById(id):
    sql = "SELECT * from products WHERE id=%s"
    params = (id,)
    cursor.execute(sql,params)
    result = cursor.fetchall()
    print(result)

getProductById(3)