from bs4 import BeautifulSoup as be4

with open("index.html", encoding="utf-8") as file:
    html = file.read()

obj = be4(html, "html.parser")

print("--------------find attributes-------------")
sonuc = obj.find(id="item2")
print(sonuc)

print("--------------find_all attributes-------------")
sonuc = obj.find_all(class_="item")
print(sonuc)

print("---------select----------")
sonuc = obj.select("#header")
print(sonuc)

sonuc = obj.select("#item1")
print(sonuc)

print("------------------------------------")
#bütün uyan hepsini getirir nokta class ifade eder.
sonuc = obj.select(".item")
print(sonuc)

print("-----------------select_one .-------------------")
#bütün uyan hepsini getirir nokta class ifade eder.
sonuc = obj.select_one(".item")
print(sonuc)

print("-----------------select_one #-------------------")
#bütün uyan hepsini getirir nokta class ifade eder.
sonuc = obj.select_one("#item2")
print(sonuc)

print("------------------obj.div.attrs---------------")
#tek olacagı için string olarak verir
sonuc = obj.div.attrs["id"]
print(sonuc)

#class tek olamayacagı için dict verir 
sonuc = obj.div.attrs["class"]
print(sonuc)

print("-----------------obj.div.get_text--------------")
sonuc = obj.div.get_text()
print(sonuc)

sonuc = obj.ul.get_text(strip=True ,separator="-")
print(sonuc)

print("------------------for döngüsü ile butun hepsini alma")
for a in obj.find_all("a"):
    print(a.get("href"))