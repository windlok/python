import json
product = {
    "id": 6,
    "title":"macbook pro",
    "price": 1299,
    "rating": 4.5,
    "category": "bilgisayar",
    "colors": ["red","blue","black"]
}

print(product)
print(type(product))
print(product["id"])

#serialize --> encode etmek
#neden serialize yaparız? --> json formatında bir string'e çevirmek için serialize yaparız. json formatında bir string'e çevirmek için json.dumps() kullanılır.

sonuc =json.dumps(product)

print(sonuc)
print(type(sonuc))
#print(sonuc["id"]) #TypeError: string indices must be integers

with open("product.json","w",encoding="utf-8") as file:
    json.dump(product,file,ensure_ascii=False,indent=2) 
    #indent=2 ile json dosyasını daha okunabilir hale getiririz. Her bir key-value çifti 2 boşlukla girintilenir.
    #ensure_ascii=False ile Türkçe karakterlerin düzgün bir şekilde yazılmasını sağlar. Eğer ensure_ascii=True olursa Türkçe karakterler Unicode kodlarına dönüştürülür ve okunması zorlaşır.
