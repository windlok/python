import random

class Sensor:
    def __init__(self,sensor_adi,baglanti_pini):
        self.sensor_adi=sensor_adi
        self.baglanti_pini=baglanti_pini
        self.ham_veriler=[]
        self.kalibrasyon_carpani=1.0
        
    def veri_ekleme(self,deger):
        self.ham_veriler.append(deger)
    
    def kalibrasyon_ayarla(self,yenicarpan):
        self.kalibrasyon_carpani=yenicarpan
        print(f"kalibrasyon carpani olarak güncellendi: {self.kalibrasyon_carpani}")

    def veri_temizleme(self,altlimit,ustlimit):
        self.altlimit=altlimit
        self.ustlimit=ustlimit
        self.gecerliveriler=[]

        for veri in self.ham_veriler:
            if veri >= self.altlimit and veri <= self.ustlimit:
                self.gecerliveriler.append(veri)
            self.safveri=self.gecerliveriler
        print("filtreleme basarili")            

    def gercek_agirligi_hesapla(self):
        if len(self.gecerliveriler)!=0:
            mean=sum(self.gecerliveriler)/len(self.gecerliveriler)
            sonuc=mean*self.kalibrasyon_carpani

            print(f"Net Ağirlik: {sonuc} kg")
        else:
            print("hiçbir veri gelemmistir!!")

# TEST SENARYOSU
s1 = Sensor("TC302-500N", "A0")
veriler = []
for veri in range(15):
    veriler.append(random.randint(-50,500))
# 1. Ham verileri ekleyelim (Bazıları bozuk/gürültülü)

for v in veriler:
    s1.veri_ekleme(v)

# 2. Kalibrasyon ayarla (Örn: %5 sapma var diyelim)
s1.kalibrasyon_ayarla(1.05)

# 3. Temizle (Sadece 0 ile 50 arasındaki değerleri al)
s1.veri_temizleme(0, 50)

# 4. Sonucu hesapla
s1.gercek_agirligi_hesapla()
