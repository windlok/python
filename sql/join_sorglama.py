import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0321",
    database="shopdb"
)

cursor = db.cursor()

# sql = "SELECT * FROM products"
sql = "SELECT * FROM products inner join categories on products.category_id = shopdb.categories.Id"

# cursor.execute(sql,value)
cursor.execute(sql)
result = cursor.fetchall()
print(result)