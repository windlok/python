import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0321",
    database="shopdb"
)

cursor = db.cursor()

# sql="SELECT * FROM products WHERE price>10000"
# sql="SELECT * FROM products WHERE Id>2" burada işe tek 2 den büyük olan ilk deger 
# sql="SELECT * FROM products WHERE Id>=2" 
# sql="SELECT * FROM products WHERE name='Samsung a8'" 
# sql="SELECT * FROM products WHERE name='Samsung a8' and price=3000" 
# sql="SELECT * FROM products WHERE name LIKE '%Samsung%'" #%Samsung% içinde Samsung geçen tüm ürünleri getirir 
# sql = "SELECT * FROM products WHERE name LIKE 'S%'" #S ile başlayan tüm ürünleri getirir
# sql = "SELECT * FROM products WHERE name LIKE '%S'" #S ile biten tüm ürünleri getirir

id=2
sql="SELECT * FROM products WHERE Id=%s"
params =(id,) 

result = cursor.execute(sql, params)

for row in cursor.fetchall():
    print(row)


def getProductsByName(name):
    sql = "SELECT * FROM products WHERE name LIKE %s"
    params = ('%' + name + '%',)
    cursor.execute(sql, params)
    return cursor.fetchall()

products = getProductsByName("Samsung")