import requests as req

response = req.post('https://jsonplaceholder.typicode.com/posts',data={
    "userId":"1",
    "title":"deneme",
    "body":"deneme ileti"
})

sonuc = response
print(sonuc)
#2xx durum kodları başarılı işlemi ifade eder
print(sonuc.text)