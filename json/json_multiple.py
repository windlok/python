db={
    "users":{
        "mustafatastay":{
            "firstname":"mustafa",
            "lastname":"tastay"
        },
        "mehmettastay":{
            "firstname":"mehmet",
            "lastname":"tastay"
        },
    },
    "products":{
        "1": {
            "title": "asus laptop",
            "price": 999
        },
        "2": {
            "title": "lenovo laptop",
            "price": 899
        }
    }

}

import json

# with open("db.json","w",encoding="utf-8") as file:
#     json.dump(db,file,ensure_ascii=False,indent=2)

with open("db.json") as file:
    data=json.load(file)

print(data["users"])
print(data["products"])

data["products"].update(
    {
        "4": {
            "title": "moster laptop",
            "price": 1299
        }
    }
)

# kolonda age olmamasına ragmen ekleyebiliyoruz
data["users"].update(
    {
        "ayse": {
            "firstname": "ayse",
            "lastname": "tastay",
            "age": 25
        }
    }
)

with open("db.json","w",encoding="utf-8") as file:
    json.dump(data,file,ensure_ascii=False,indent=2)