sayilar = [1, 2, 3, 4, 5]

sonuc = list(filter(lambda x: x % 2 == 0, sayilar))
sonuc1 = list(filter(lambda x: x % 2 == 0, sayilar))
print(sonuc)
print(sonuc1)

isimler = ["Ali", "Veli", "Ayşe", "Fatma"]

sonuc2 = list(filter(lambda x: len(x) > 3, isimler))
print(sonuc2)   

sonuc3 = list(map(lambda x: x.upper(), sonuc2))
print(sonuc3)


user = [
    {
        "name": "Ali",
        "posts": [
            {"id": 1, "title": "Python"},
            {"id": 2, "title": "JavaScript"},
            {"id": 3, "title": "Java"}
        ]
    },
    {
        "name": "Veli",
        "posts": [
            {"id": 1, "title": "Python"},
            {"id": 2, "title": "JavaScript"},
            {"id": 3, "title": "Java"}
        ]
    }
]

sonuc4 = list(filter(lambda x: x["name"] == "Ali", user))
sonuc5=list(map(lambda x: x["posts"], sonuc4))
print(sonuc5)

sonuc6 = list(map(lambda user: user["posts"], sonuc4))
print(sonuc6)