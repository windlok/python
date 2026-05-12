import requests
from bs4 import BeautifulSoup as be4
from csv import writer

url="https://www.youtube.com"

#sanki tarayıcıyı taklit eden gibi hata almasını engellemek için
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

html = be4(response.text, "html.parser")

container = html.find(id="content")
if container:
    cihazlar = container.find_all(class_="ytLockupViewModelContentImage")
    print(len(cihazlar))
else:
    print("İstenen ID bulunamadı. Sayfa dinamik yükleniyor olabilir.")

with open("n11_cihazlar.csv","w" ,encoding="utf-8") as file:
    csv_write = writer(file)
    csv_write.writerow(["cihaz_adi","fiyat"])
    
    for cihaz in cihazlar:
        cihaz_adi = cihaz.find(class_="product-item-title two-lines").text.strip()
        cihaz_fiyat = cihaz.find(class_="price-currency").text.strip()
        print(cihaz_adi, cihaz_fiyat)
        csv_write.writerow([cihaz_adi,cihaz_fiyat])
