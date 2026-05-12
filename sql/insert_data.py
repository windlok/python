import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0321",
    database="shopdb"
)

cursor = db.cursor()

sql = "INSERT INTO products (name, price,imageurl,description) VALUES (%s, %s, %s, %s)"
# value = ("iPhone 13", 999.99, "https://example.com/iphone13.jpg", "The latest iPhone with A15 Bionic chip.")
values = [
    ("samsung a6", 999.99, "https://example.com/samsung.jpg", "The latest Samsung with A15 Bionic chip."),
    ("samsung a7", 1999.99, "https://example.com/samsung.jpg", "The latest Samsung with A14 Bionic chip."),
    ("samsung a8", 2999.99, "https://example.com/samsung.jpg", "The latest Samsung with A13 Bionic chip."),
]

# cursor.execute(sql,value)
cursor.executemany(sql,values)

try:
    db.commit()
    print(cursor.rowcount, "record inserted.")

except mysql.connector.Error as err:
    print("Error: {}".format(err))
finally:
    cursor.close()
    db.close()
    print("Database connection closed.")

