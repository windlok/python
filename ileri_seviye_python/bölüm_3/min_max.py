sayilar = [5, 2, 9, 1, 5, 6]
harfler = ['e', 'i', 'o', 'u' , 'ada','ada1']

sonuc = max(sayilar)
print("En büyük sayı:", sonuc)

sonuc = min(sayilar)
print("En küçük sayı:", sonuc)


sonuc = max(harfler)
print("En büyük harf:", sonuc)

sonuc = min(harfler)
print("En küçük harf:", sonuc)
# max ve min fonksiyonları, sıralama kurallarına göre çalışır. 
# Sayılar için büyüklük sırasına göre, harfler için alfabetik sıraya göre değerlendirme yapar.

sonuc = min(len(harfler) for harf in harfler)
print("En kısa harf uzunluğu:", sonuc)

sonuc = max(len(harf) for harf in harfler)
print("En uzun harf uzunluğu:", sonuc)

urunler = [
    {"ad": "Laptop", "fiyat": 5000},
    {"ad": "Telefon", "fiyat": 7000},
    {"ad": "Tablet", "fiyat": 2000}
]

en_pahali_urun = max(urunler, key=lambda urun: urun["fiyat"])
print("En pahalı ürün:", en_pahali_urun["ad"], "Fiyat:", en_pahali_urun["fiyat"])
