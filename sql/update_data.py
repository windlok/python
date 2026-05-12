import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0321",
    database="shopdb"
)

cursor = db.cursor()

# sql = "UPDATE products SET name = 'samsung a8-updated' WHERE name = 'samsung a8'"

# try:
#     db.commit()
#     print(cursor.rowcount, "record(s) affected")
# except mysql.connector.errors as err:
#     db.rollback()
#     print(err)

# finally:
#     db.close()
#     cursor.close()

def updateProduct(names,name):
    sql = "UPDATE products SET name = %s WHERE name = %s"
    params = (names,name)
    cursor.execute(sql, params)
    try:
        db.commit()
        print(cursor.rowcount, "record(s) affected")
    except mysql.connector.errors as err:
        db.rollback()
        print(err)
    finally:
        db.close()
        cursor.close()
updateProduct("samsung s25-updated","samsung s25")