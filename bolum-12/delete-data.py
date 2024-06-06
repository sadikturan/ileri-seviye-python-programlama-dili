import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sadikturan_41",
    database = "shopdb"
)

cursor = db.cursor()

def deleteProductById(id):
    sql = "DELETE FROM products WHERE id=%s"
    params = (id,)
    # sql = "DELETE FROM products WHERE name LIKE '%s23%'"
    cursor.execute(sql, params)

    try:
        db.commit()
        print(f"{cursor.rowcount} tane kayıt silindi")
    except mysql.connector.Error as err:
        print(err)
    finally:
        db.close()
        cursor.close()

deleteProductById(3)