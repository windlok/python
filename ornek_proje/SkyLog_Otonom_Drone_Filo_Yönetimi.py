

class Drone:
    def __init__(self,drone_id,max_kapasite):
        self.drone_id=drone_id
        self.max_kapasite=max_kapasite
        self.batarya_yuzdesi=100
        self.durum="beklemede"
        self.mevcutyuk=0

    def sarj_et(self):
        
        if self.batarya_yuzdesi==100:
            print(f"drone {self.drone_id} tamamen dolu ucusa hazir")
        else:
            kalan_Sarj=100-self.batarya_yuzdesi
            print(f"pil: {self.batarya_yuzdesi} dolmasi gerekiyor gerekli dk: {kalan_Sarj * 6}")
            self.batarya_yuzdesi=100
            print("dolum gerceklesti pil 100%")
        

    def yuk_al(self,kilo):
        if kilo<=self.max_kapasite:
            self.mevcutyuk=kilo
            print(f"kilo {kilo} tasimak icin uygundur")
        else:
            print(f"kilo {kilo} toplam kapasitenin {self.max_kapasite} ustunde")    
    #yanlıs kullanım 
    def ucus_basla(self):
        if self.batarya_yuzdesi > 20 and self.mevcutyuk <= self.max_kapasite:
            self.durum="ucusta"
            self.batarya_yuzdesi -=30
            print(f'{self.drone_id} numarali dron kalkis yapti pil {self.batarya_yuzdesi}')
        else :
            print(f"❌ Uçuş iptal! Şartlar sağlanmadı. Pil: %{self.batarya_yuzdesi}, Yük: {self.mevcutyuk} kg")           

class Filo():##__init__ dron olusturmalıyım 
    def __init__(self):
        self.dronlar=[]
        
    def drone_ekle(self,yenidron):
        self.dronlar.append(yenidron)
        print(f"Yeni dron eklendi: {yenidron.drone_id}")

    def uygun_drone_bul(self,kargokilo):
        self.kargokilo=kargokilo

        for dron in self.dronlar:
            if dron.batarya_yuzdesi>=60 and dron.durum=="beklemede" and dron.max_kapasite >= kargokilo:
                print(f"{dron.drone_id} id dron {dron.durum}")

                return dron
        print("kimse bulunamadı")

    def filo_raporu(self):
        print("\n--- 🌐 SKYLOG ANLIK FİLO RAPORU ---")
        for bilgi in self.dronlar:
            print(f'dron id: {bilgi.drone_id} batarya yüzdesi: {bilgi.batarya_yuzdesi}\n kapasitesi: {bilgi.max_kapasite} durumu: {bilgi.durum} mevcut yük: {bilgi.mevcutyuk}')
        print("----------------------------------")
# Sınıf tanımlamaların (Drone ve Filo) yukarıda aynen kalıyor...
# Sadece Filo'nun init'ini def __init__(self): olarak düzelt.

# 1. Önce Kargo Şirketimizi (Filo) kuruyoruz (1 tane yeterli)
skylog_filosu = Filo()

# 2. Şimdi fabrikadan Dronlarımızı (Robotları) üretiyoruz
d1 = Drone(1, 10)  # ID'si 1, Kapasitesi 10 kg
d2 = Drone("DJI_Mavic", 9) # ID'si DJI_Mavic, Kapasitesi 5 kg
d3 = Drone("Mini_4K", 2)   # ID'si Mini_4K, Kapasitesi 2 kg

# 3. Ürettiğimiz dronları şirketimizin garajına (filoya) ekliyoruz
skylog_filosu.drone_ekle(d1)
skylog_filosu.drone_ekle(d2)
skylog_filosu.drone_ekle(d3)
skylog_filosu.uygun_drone_bul(3)

# 4. Bir dronu test edelim!
d1.yuk_al(5)       # 5 kilo yükleyelim
d1.ucus_basla() 
d1.ucus_basla()
d2.ucus_basla()
d3.ucus_basla()
skylog_filosu.filo_raporu()

