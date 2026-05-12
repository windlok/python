import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0321",
    database="shopdb"
)

cursor = db.cursor()

sql = "DELETE FROM products WHERE name = 'samsung s25-updated'"

cursor.execute(sql)

try:
    db.commit()
    print(cursor.rowcount, "record(s) affected")

except mysql.connector.errors as err:
    db.rollback()
    print(err)

finally:
    db.close()
    cursor.close()

    #id tek parametre olarak oldugunda ıd sağına (virgül) konur parametrelerde yapılır