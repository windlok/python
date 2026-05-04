from bs4 import BeautifulSoup as be4

with open("index.html", encoding="utf-8") as file:
    html = file.read()

obj = be4(html, "html.parser")

sonuc = obj.body.div.contents[3]
print(sonuc)

print("---------------children--------")
for i in obj.body.div.children:
    print(i)


print("---------------parent--------")
sonuc = obj.body.h2.parent
print(sonuc)

print("---------------parent.parent--------")
sonuc = obj.body.h2.parent.parent
print(sonuc)

print("---------------next_element--------")
sonuc = obj.body.ul.next_element.next_element
print(sonuc)

print("---------------next_sibling--------")
sonuc = obj.body.ul.next_sibling.next_sibling
print(sonuc)

print("--------------------find_next_sibling-------------------")
sonuc = obj.body.div.find_next_sibling("div")
print(sonuc)

print("--------------------find_next_sibling den find_next_sibling-------------------")
sonuc = obj.body.div.find_next_sibling("div").find_next_sibling("div").find_previous_sibling("div")
print(sonuc)

