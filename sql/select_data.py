import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0321",
    database="shopdb"
)

cursor = db.cursor()

sql = "SELECT * FROM products"

#filtreleme yapmak istersek
sql = "SELECT Id,name FROM products"

cursor.execute(sql)

#tablonun tamamını getirir
# result = cursor.fetchall()
# for row in result:
#     # print(row)
#     print(f"ID:{row[0]} Name:{row[1]}")

# print("********************")
#tablonun ilk elemanını getirir
results = cursor.fetchone()
print(results)

