# Koşul ifadeleri (if-else)
for i in range(1,11):
    if i % 2 == 0:
        print(i)

# List comprehension ile aynı işlemi yapalım
sonuc = [i for i in range(1,11) if i % 2 == 0]
print(sonuc)

sayilar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cift_sayilar = []

for sayi in sayilar:
    if sayi % 2 == 0:
        cift_sayilar.append(sayi)


cift_sayilar_lc = [sayi for sayi in sayilar if sayi % 2 == 0]

print(cift_sayilar)
print(cift_sayilar_lc)



sonuc = [i if i % 2 == 0 else "Tek" for i in range(1,11)]
print(sonuc)


urunfiyatlari = [0.1, 0.2, 0.3, 0.4, 0.5]
vergiler=[]
for fiyat in urunfiyatlari:
    if fiyat > 0.3:
        vergiler.append("vergiler yüksek")
    else:
        vergiler.append(fiyat)

vergiler_lc = [0.3 if vergi < 0.3 else vergi for vergi in urunfiyatlari]
vergiler_lc1= [0.3 for fiyat in urunfiyatlari if fiyat < 0.3 ]
print(vergiler)
print(vergiler_lc)
print(vergiler_lc1)