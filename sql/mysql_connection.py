import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0321",
    database="shopdb"
)

cursor = db.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
# cursor.execute("SHOW DATABASES")
cursor.execute("CREATE TABLE category (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
cursor.execute("SHOW TABLES")

for i in cursor:
    print(i)