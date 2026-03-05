sonuc = all([True, True, True])
print(sonuc)

#all() fonksiyonu verilen iterable içindeki tüm elemanların True olup olmadığını kontrol eder. 
# Eğer tüm elemanlar True ise True döner, aksi takdirde False döner.
sonuc1 = all([True, False, True])
print(sonuc1)

#any() fonksiyonu verilen iterable içindeki herhangi bir elemanın True olup olmadığını kontrol eder. 
# Eğer herhangi bir eleman True ise True döner, aksi takdirde False döner.
sonuc2 = any([False, False, False])
print(sonuc2)

sonuc3 = any([False, True, False])
print(sonuc3)

#and => True and True => all() fonksiyonu gibi çalışır, tüm elemanların True olması gerekir.
#or => True or False => any() fonksiyonu gibi çalışır, herhangi bir elemanın True olması yeterlidir.

sayilar = [1, 2, 3, 4, 5]

sonuc4 = all(sayi > 4 for sayi in sayilar)
print(sonuc4)

sonuc5 = any(sayi > 3 for sayi in sayilar)
print(sonuc5)

user = ["ahmet", "mehmet", "ayşe", "fatma"]

sonuc6 =[user[0] == "a" for user in user]
print(sonuc6)

sonuc7 = all(user[0] == "a" for user in user)
print(sonuc7)

sonuc8 = any(user[0] == "a" for user in user)
print(sonuc8)