from bs4 import BeautifulSoup as be4

with open("index.html") as file:
    html = file.read()

obj = be4(html,"html.parser")

sonuc = obj 

#prettify girintileri ayarlanmış sekilde gösterir.
sonuc = obj.prettify()

sonuc = obj.title.name

sonuc = obj.body.h1.string

sonuc = obj.head.title.string

#sayfada buldugu ilk element
sonuc = obj.body
print(sonuc)

