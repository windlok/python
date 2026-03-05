ilanlar = [
    {"urun": "MacBook Air", "fiyat": 15000, "hasarli_mi": False},
    {"urun": "DJI Mavic Mini", "fiyat": 4000, "hasarli_mi": True},
    {"urun": "Dell Inspiron Laptob", "fiyat": 12000, "hasarli_mi": False},
    {"urun": "DJI Mini 4K", "fiyat": 18000, "hasarli_mi": False},
    {"urun": "Kırık Ekranlı Telefon", "fiyat": 2000, "hasarli_mi": True},
    {"urun": "Oyun Bilgisayarı", "fiyat": 35000, "hasarli_mi": False}
]

# print(len(ilanlar))
# sağlam ürünler
saglam = [ilan["urun"] for ilan in ilanlar if ilan["hasarli_mi"]==False]
print(saglam)
# hasarli = [  for hasar in ilan["hasarli_mi"] if hasar==False ]
# print(hasarli)

# fiyatı 20000'den düşük olan sağlam ürünler
cift = [ilan["urun"] for ilan in ilanlar if ilan["hasarli_mi"]==False if ilan["fiyat"] <= 20000]
print(cift)

# fiyatı 20000'den düşük olan sağlam ürünler ve kar marjı
kar = [(ilan["urun"], ilan["fiyat"]*0.2) for ilan in ilanlar if ilan["hasarli_mi"]==False if ilan["fiyat"] <= 20000]
print(kar)