sayilar = [5, 2, 9, 1, 5, 6]

# Sıralama işlemi yaparak listeyi düzenleyelim ama orijinal listeyi değiştirmeden yeni bir liste olusturur.
sayilar.sort()
print(sayilar)  # Çıktı: [1, 2, 5, 5, 6, 9]

sayilar = [5, 2, 9, 1, 5, 6]
# sorted() fonksiyonu ile sıralama yaparak yeni bir liste oluşturur.
sirali_sayilar = sorted(sayilar , reverse=True)  # reverse=True ile büyükten küçüğe sıralama yapar.
print(sirali_sayilar)  # Çıktı: [9, 6, 5, 5, 2, 1]
print(sayilar)  # Orijinal liste değişmediği için çıktısı: [5, 2, 9, 1, 5, 6]


users = [
    {"username":"musatafa","posts ":["post1","post2"],"email":"info@abc.com"},
    {"username":"ayse","posts ":["post3"],"email":"infoabc.com"},
    {"username":"mehmet","posts ":["post4","post5","post6"],"email":"infoabc.com"}
]
print(users)

sonuc = sorted(users , key=len , reverse=True)  # posts sayısına göre sıralama yapar.
print(sonuc)  

sonuc1 =sorted(users , key=len)
print(sonuc1)

sonuc2 = sorted(users, key=lambda user: len(user["posts "]), reverse=True)  # posts sayısına göre sıralama yapar.
print(sonuc2)

sonuc3 =map(lambda user: user["username"], sorted(users, key=lambda user: len(user["posts "]), reverse=True))  # Sadece username'leri alır.
print(list(sonuc3))  # Çıktı: ['mehmet', 'musatafa', 'ayse']

kurslar = [{
    "kurs_adi":"python","egitmen":"mustafa","ogrenci_sayisi":100},
    {"kurs_adi":"java","egitmen":"ayse","ogrenci_sayisi":150},
    {"kurs_adi":"javascript","egitmen":"mehmet","ogrenci_sayisi":120}
    ]

sonuc4 = sorted(kurslar , key=lambda kurs: kurs["ogrenci_sayisi"] , reverse=True)  # ogrenci sayısına göre sıralama yapar.
print(sonuc4)

sonuc5 = sorted(kurslar , key=lambda kurs: kurs["kurs_adi"])  # kurs adına göre sıralama yapar.
print(sonuc5)

sonuc6 =map(lambda kurs: kurs["kurs_adi"], sorted(kurslar , key=lambda kurs: kurs["ogrenci_sayisi"] , reverse=True))  # Sadece kurs adlarını alır.
print(list(sonuc6))  # Çıktı: ['java', 'javascript', 'python']