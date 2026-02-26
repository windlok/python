class Parca:
    def __init__(self,isim,kategori,stokadedi):
        self.isim=isim
        self.kategori=kategori
        self.stokadedi=stokadedi
        self.arizaliadet=0

    def ariza_bildir(self,adet):
        if adet <= self.stokadedi:
            self.arizaliadet += adet
            self.stokadedi -= adet

class   Laboratuvar:
    def __init__(self):
        self.envanter=[]


    def parca_kaydet(self,yeniparca):
        self.envanter.append(yeniparca)

    def kritik_stok_raporu(self):
        for urun in self.envanter: 
            if urun.stokadedi <= 3:
                print(f"DİKKAT! {urun.isim} adlı parçadan sadece {urun.stokadedi} adet kaldı.")
                
    def urun_bilgisi(self):
        for urun in self.envanter:
            print(f'urunun adi:{urun.isim} kategorisi: {urun.kategori} stok adeti: {urun.stokadedi} arizali adet: {urun.arizaliadet}')
muta_labs=Laboratuvar()

p1 = Parca("PhidgetSBC4", "Mikrodenetleyici", 10)
p2 = Parca("LVM-110 Karti", "Modül", 2)       # Zaten kritik stokta
p3 = Parca("M12-50 LVDT", "Sensör", 5)

p1.ariza_bildir(7)
p2.ariza_bildir(3)
p3.ariza_bildir(1)

muta_labs.parca_kaydet(p1)
muta_labs.parca_kaydet(p2)
muta_labs.parca_kaydet(p3)


print("------Paketler--------")
muta_labs.urun_bilgisi()

print("\n--- KRİTİK STOK RAPORU ---")
muta_labs.kritik_stok_raporu()

