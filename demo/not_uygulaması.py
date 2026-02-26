#kulanıcıdan ad soyad bilgisi 3 not bilgisii v final but gibi bunlarıda dosyaya kaydecegiz

class kullanici:
    def __init__(self,ad,soyad,vize,final,but):
        self.ad=ad
        self.soyad=soyad
        self.vize=vize
        self.final=final
        self.but=but
        
    def arttir(self):
        self.id=0
        id +=1

    def v_not_duzenleme(self,puan,dusurme):
        if dusurme=="evet":
            if puan <= 100 and puan >= 0:
                self.vize =puan
                print(f"islem basarili yeni puan {self.vize}") 
                
            else:
                print(f"dusurme islemi yapilamaz {puan} degistirmek istedigin {self.vize}")  
        else:
            if puan <= 100 and puan >= 0:
                self.vize =puan
                print(f"islem basarili {self.vize}")
            else:
                 print(f"yukseltme islemi yapilamaz {puan} degistirmek istedigin {self.vize}")     

    def f_not_duzenleme(self,puan,dusurme):
        if dusurme=="evet":
            if puan <= 100 and puan >= 0:
                self.final =puan
                print(f"islem basarili yeni puan {self.final}") 
                
            else:
                print(f"dusurme islemi yapilamaz {puan} degistirmek istedigin {self.final}")  
        else:
            if puan <= 100 and puan >= 0:
                self.final =puan
                print(f"islem basarili {self.final}")
            else:
                 print(f"yukseltme islemi yapilamaz {puan} degistirmek istedigin {self.final}")   

class dosya_kayit:
    def __init__(self):
        self.liste=[]

    def yeni_kayit(self,yeni):
        self.liste.append(yeni) 
        file = open("demo/kullaniciler.txt", "a", encoding="utf-8")
        file.write(str(yeni.ad) + " " + str(yeni.soyad) + " " + str(yeni.vize) + " " + str(yeni.final) + " " + str(yeni.but) + "\n")
        file.close()    
    
    def kayitlari_goster(self):
        with open("demo/kullaniciler.txt", "r", encoding="utf-8") as file:
            print(file.read())
        
class puanlama:
    def __init__(self):
        self.liste=[]

    def yeni_not(self,puan):
        self.liste.append(puan)
        
                    
    def puan_hesaplama(self):
        for puan in self.liste:
            v=float(puan.vize)*0.4
            f=float(puan.final)*0.6
            b=float(puan.but)*0.6
            s=v+f
            s1=v+b
            if s <= 60:
                if s1 <= 60:
                    print(f"kaldiniz notunuz {s} ortalamanin altinda hocayla iletisime geciniz")
                else:
                    print(f"bütte gectiniz ortalamaniz {s1}")
            else:
                print(f'gectiniz ortalamaniz {s} ortalamanin ustunde')


kullanici_listesi = []
puanlama_listesi = []

def secim():
    while True:
        sec = int(input("1) Yeni kayıt\n2) Not düzenleme\n3) Kullanıcı kaydetme\n4) Kayıtlı kullanıcıları gör\n5) Çıkış\nSeçim: "))
        if sec == 1:
            ad = input("Ad: ")
            soyad = input("Soyad: ")
            vize = int(input("Vize: "))
            final = int(input("Final: "))
            but = int(input("Büt: "))
            yeni_kul = kullanici(ad, soyad, vize, final, but)
            kullanici_listesi.append(yeni_kul)
            print("Kullanıcı eklendi.")
        elif sec == 2:
            for i, kul in enumerate(kullanici_listesi):
                print(f"{i+1}) {kul.ad} {kul.soyad}")
            secim_no = int(input("Düzenlemek istediğiniz kullanıcı numarası: ")) - 1
            duz2 = input("Düşürmek mi istiyorsunuz? (evet/hayir): ")
            duz1 = int(input("Yeni notu giriniz: "))
            kullanici_listesi[secim_no].f_not_duzenleme(duz1, duz2)
        elif sec == 3:
            for kul in kullanici_listesi:
                k = dosya_kayit()
                k.yeni_kayit(kul)
            print("Tüm kullanıcılar dosyaya kaydedildi.")
        elif sec == 4:
            k = dosya_kayit()
            k.kayitlari_goster()
        elif sec == 5:
            break
        else:
            print("Geçersiz seçim.")

secim()















