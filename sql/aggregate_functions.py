import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0321",
    database="shopdb"
)

cursor = db.cursor()

# sql = "SELECT COUNT(*) FROM products"
# sql = "SELECT AVG(price) FROM products"
# sql = "SELECT SUM(price) FROM products"
# sql = "SELECT MIN(price) FROM products"
# sql = "SELECT MAX(price) FROM products"
# sql = "SELECT name,price FROM products WHERE price=(SELECT MAX(price) FROM products)"
sql = "SELECT name,price FROM products ORDER BY price DESC LIMIT 1"

cursor.execute(sql)

# print("Total number of products:", cursor.fetchone()[0])
print("Average price:", cursor.fetchone()[0])

db.commit()