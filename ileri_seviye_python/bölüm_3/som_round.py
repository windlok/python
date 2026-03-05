sayilar = [5, 2, 9, 1, 5, 6]

sonuc = sum(sayilar) / len(sayilar)
sonuc1 = sum(sayilar,5)
print(sonuc)
print(sonuc1)

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 500},
    {"name": "Tablet", "price": 300},
    {"name": "Headphones", "price": 200},
    {"name": "Smartwatch", "price": 0}
]

toplamFiyat = sum([urun["price"] for urun in products])
urunSayisi = len([urun for urun in products if urun["price"] > 0])
sonuc3 = toplamFiyat / urunSayisi
print(toplamFiyat)
print(sonuc3)

sonuc2 = round(5.5)
print(sonuc2)

sonuc3 = round(5.4)
print(sonuc3)

sonuc4 = round(5.1231, 2)
print(sonuc4)

sonuc5 = round(5.13165, 5)
print(sonuc5)