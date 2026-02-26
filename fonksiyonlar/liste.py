kullanici = {"isim": "Eda", "yas": 24, "sehir": "Ankara"}

# items(): Sözlükteki anahtar (key) ve değerleri (value) ikili çiftler halinde gruplar.
ciftler = list(kullanici.items())  # Sonuç: [('isim', 'Eda'), ('yas', 24), ('sehir', 'Ankara')]

# items() fonksiyonunun döngüde kullanımı (En yaygın senaryo):
# for anahtar, deger in kullanici.items(): print(anahtar, ":", deger)  
# Çıktı: isim : Eda, yas : 24, sehir : Ankara
print(ciftler)