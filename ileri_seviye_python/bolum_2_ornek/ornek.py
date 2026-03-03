#1
sayilar = [j for j in range(1,100) if j % 4 == 0 if j % 3 == 0]

print(sayilar)

#2
text = "hello 12345 wordl"
sonuc = [karakter for karakter in text if karakter.isdigit()]
print(sonuc)  # ['1','2','3','4','5']

#3
sicaklik = [20,15,0,-5,-2]
buzlu = [i if i>=0 else "buzlanma tehlikesi" for i in sicaklik]
print(buzlu)

#4
ogrenciler = ["ali","ahmet","canan"]
notlar = [50,60,80]

liste = [(ogrenciler[u],notlar[u]) for u in range(0, len(ogrenciler))]
kullanici = {key:value for (key,value) in liste if value <= 60}

print(kullanici)

#5
liste=[(x,y,z) for x in range(3) for y in range(3) for z in range(2)]
print(liste)

