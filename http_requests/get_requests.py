import requests as req
import json

response = req.get('https://jsonplaceholder.typicode.com/posts')

sonuc =type(response)
print(sonuc)
print(response.status_code)
#çıktısı: 200 
print(response)

veri = json.loads(response.text)
ver = veri[0]["title"]
print(ver)

liste = []

for item in veri:
    if item["userId"] == 1:
        liste.append(item)

print(len(liste))       