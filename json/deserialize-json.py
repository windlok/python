with open("product.json") as file:
    data = file.read()

print(data)
print(type(data))
#print(data["id"]) #TypeError: string indices must be integers

#serialize --> encode etmek
#deserialize --> decode etmek

#dosyadan okuduğumuz data string formatındadır. Bunu json formatına çevirmek için json.load() kullanılır.
import json
with open("product.json") as file1:
    data1 = json.load(file1)

print(data1)
print(type(data1))
print(data1["price"]) #bu sefer çalışır çünkü data1 artık bir dictionary'dir.


#uygulama içerisinde json formatında bir string varsa bunu deserialize etmek için json.loads() kullanılır.
data2 = """
{
    "id": 1,
    "title":"macbook pro",
    "price": 1299,
    "rating": 4.5,
    "category": "laptop",
    "colors": ["red","blue","black"]
}
"""

data2 = json.loads(data2)

print(data2)
print(type(data2))
print(data2["category"])