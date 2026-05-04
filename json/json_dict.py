data = {
    "2":{
        "title":"macbook air",
        "price": 999
    },
    "3":{
        "title":"macbook pro",
        "price": 1299
    }
}

import json

#burada products.json dosyasını açıp içindeki veriyi products değişkenine atıyoruz. products değişkeni bir sözlük olacak.
with open("products1.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)


with open("products1.json") as file:
    products = json.load(file)

print(products)
print(products["2"]["title"])

#burada products sözlüğüne yeni bir eleman ekliyoruz. products sözlüğünün içine 4 adında yeni bir anahtar ekliyoruz ve bu anahtarın değeri de bir sözlük oluyor. bu sözlükte title ve price anahtarları var.
products.update({
    "4":{
        "title":"lenovo laptop",
        "price": 899
    }
})

with open("products1.json","w",encoding="utf-8") as file:
    json.dump(products,file,ensure_ascii=False,indent=2)

#burada products sözlüğünün içindeki 2 anahtarının değerini güncelliyoruz. 2 anahtarının değeri bir sözlükti. Bu sözlüğün title ve price anahtarlarının değerlerini güncelliyoruz.
products.update({
    "2":{
        "title":"asus laptop",
        "price": 999
    }
})

with open("products1.json","w",encoding="utf-8") as file:
    json.dump(products,file,ensure_ascii=False,indent=2)

#burada products sözlüğünün içindeki 3 anahtarını siliyoruz. 3 anahtarının değeri bir sözlükti. Bu sözlüğü siliyoruz.
products.pop("3")

with open("products1.json","w",encoding="utf-8") as file:
    json.dump(products,file,ensure_ascii=False,indent=2)

