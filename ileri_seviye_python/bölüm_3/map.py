sayilar = [1,2,3,4,5]
sayilar_Str = ["1","2","3","4","5"]
isimler = ["Ali","Veli","Ayşe","Fatma"]
kullanicilar=[
    {"ad":"Ali","yas":30},
    {"ad":"Veli","yas":25},
    {"ad":"Ayşe","yas":28},
    {"ad":"Fatma","yas":22}
]

kareler = []

for sayi in sayilar:
    kareler.append(sayi**2)


print(kareler)

def kareal(sayi):
    return sayi**2

sonuc=map(kareal, sayilar)
print(list(sonuc))


sonuc =map(lambda x: x**2, sayilar)
print(list(sonuc))

sonuc2 = map(int, sayilar_Str)
print(list(sonuc2))

sonuc3 = map(str.upper, isimler)
print(list(sonuc3))

sonuc4 = map(lambda kullanici: kullanici["ad"], kullanicilar)
print(sonuc4)