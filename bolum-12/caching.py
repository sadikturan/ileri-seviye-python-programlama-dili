import mysql.connector
import time
from cachetools import cached,TTLCache

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sadikturan_41",
    database = "shopdb"
)

@cached(cache=TTLCache(maxsize=32, ttl=60))
def getProducts():
    cursor = db.cursor()
    sql = "SELECT p.name,c.name from products p inner join categories c on p.categoryid=c.id WHERE c.name='Bilgisayar'"
    cursor.execute(sql)
    print("from sql")
    return cursor.fetchall()

s = time.time()
print(getProducts())
print("geçen zaman:", time.time() - s)

s = time.time()
print(getProducts())
print("geçen zaman:", time.time() - s)

s = time.time()
print(getProducts())
print("geçen zaman:", time.time() - s)