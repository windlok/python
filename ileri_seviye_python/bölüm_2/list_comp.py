sayilar = []

# 0'dan 9'a kadar olan sayıların karelerini sayilar listesine ekleyelim
for i in range(10):
    sayilar.append(i**2)

# List comprehension kullanarak aynı işlemi yapalım
sayilar_lc = [i**2 for i in range(10)]

print("Normal for döngüsü ile oluşturulan liste:", sayilar)
print("List comprehension ile oluşturulan liste:", sayilar_lc)

kurum = "SkyLog"

# List comprehension kullanarak kurum adındaki harfleri büyük harfe çevirelim
sonuc=[harf.upper() for harf in kurum]
print(sonuc)