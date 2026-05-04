from bs4 import BeautifulSoup as be4

with open("index.html", encoding="utf-8") as file:
    html = file.read()


obj = be4(html,"html.parser")

sonuc = obj.div

print("-------------------find----------------------\n")

#farkı find çok farklı özellikleri olması
sonuc = obj.find("div")
print(sonuc)

#bütün divleri gösterir
print("-------------------find_all----------------------\n")
sonuc = obj.find_all("div")
print(sonuc)

sonuc = obj.find_all("div")[1].ul
print(sonuc)

print("--------------------find_all içinde find_all---------------------\n")
sonuc = obj.find_all("div")[1].ul.find_all("li")[2]
print(sonuc)

print("--------------------find_all for döngüsü---------------------\n")
for div in obj.find_all("div"):
    if div.h2.a is not None:
        #a etiketi varsa a etiketinin içindeki yazıyı yazdırır hepsinde a etiketi yok o yüzden if ile kontrol ediyoruz
        print(div.h2.a.string.strip())
    else:
        print(div.h2.string.strip())

print("--------------------find_all for döngüsü---------------------\n")
#sadece a etiketlerinin içindeki yazıları yazdırır
for a in obj.find_all("a"):
    print(a.string.strip())