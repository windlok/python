import requests as req
import json

#hangi vakti istiyyorsak url sonundaki kısmı ona göre değiştiriyoruz current.json, forecast.json, history.json
url ="http://api.weatherapi.com/v1/current.json"
key = "5b428009f94c41fc91575016260405"

sehir = input("sehir: ")

request=req.get(url,params={
    "key":key,
    "q":sehir,
    "lang":"tr"
    })

sonuc = request.json()
sehir_adi = sonuc["location"]["name"]
hava_durumu = sonuc["current"]["temp_c"]
text = sonuc["current"]["condition"]["text"]

print(f"{sehir_adi} şu anda {hava_durumu} derece ve hava {text}")