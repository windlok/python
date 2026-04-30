data = [
    {
        "id": 1,
        "title":"apple5s",
        "price": 500,
        "rating": 4.5,
        "category": "telefon",
        "colors": ["red","blue","black"]
    },
    {
        "id": 2,
        "title":"samsung s20",
        "price": 1000,
        "rating": 4.7,
        "category": "telefon",
        "colors": ["red","blue","black"]
    },
    {
        "id": 3,
        "title":"macbook pro",
        "price": 1299,
        "rating": 4.5,
        "category": "laptop",
        "colors": ["red","blue","black"]
    }
]
import json
with open("products.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)
    
    #w ile yazma modunda açarız. Eğer dosya yoksa oluşturur, varsa içeriğini siler ve yeni veriyi yazar.
    #a ile ekleme modunda açarız. Eğer dosya yoksa oluşturur, varsa içeriğini silmeden yeni veriyi ekler.

data1= {
        "id": 4,
        "title":"lenovo laptop",
        "price": 899,
        "rating": 4.3,
        "category": "laptop",
        "colors": ["red","blue","black"]
    }

#böyle yaparsakta olmaz kaydetme direkt append yapmış gibi olur. json dosyası bozulur. json dosyasında bir liste varsa bu listeye yeni bir eleman eklemek ist
# with open("products.json","a",encoding="utf-8") as file:
#     json.dump(data1,file,ensure_ascii=False,indent=2)

data2= {
        "id": 5,
        "title":"asus laptop",
        "price": 999,
        "rating": 4.4,
        "category": "laptop",
        "colors": ["red","blue","black"]
    }

with open("products.json") as file:
    producks = json.load(file)

producks.append(data2)

with open("products.json","w",encoding="utf-8") as file:
    json.dump(producks,file,ensure_ascii=False,indent=2)