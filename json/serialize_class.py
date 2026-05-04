class product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

# @serialize
# p1 = product(1, "asus laptop", 999)
# p2 = product(2, "lenovo laptop", 899)

# # products = [p1.__dict__, p2.__dict__]

# products ={
#     p1.id: p1.__dict__,
#     p2.id: p2.__dict__
# }

import json

# #bunu __dict__ ile yapıyoruz neden cunku json.dump() fonksiyonu sadece dict tipini kabul eder ve biz de class'ımızı dict'e çevirmek için __dict__ kullanırız
# with open("serialize_class.json", "w", encoding="utf-8") as file:
#     json.dump(products, file, ensure_ascii=False, indent=2)

# @deserialize

with open("serialize_class.json") as file:
    products = json.load(file)
print(type(products))
urunler = []

for key, value in products.items():
    urunler.append(product(key, value["name"], value["price"]))

print(type(urunler))
for urun in urunler:
    print(f"id: {urun.id}, name: {urun.name}, price: {urun.price}")