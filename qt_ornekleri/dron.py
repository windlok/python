from time import time
import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow , QToolTip
from MainWindow import Ui_MainWindow


class dron():
    ui=Ui_MainWindow()
    def __init__(self,ad,pil):
        self.id=0
        self.dron_adi=ad
        self.dron_pil=pil
        self.dron_kilo=0
        self.dron_aktif="evet"
        self.dron_max_kilo=10

    def yuk_al(self,gelen_kilo):
        self.dron_mevcut_kilo = gelen_kilo
        if self.dron_mevcut_kilo <= self.dron_max_kilo:
            print(f'uçus için uygundur {self.dron_mevcut_kilo} kilo tasimak icin uygundur')
        else:
            print(f'yuk {self.dron_kilo} üstünde')

    def ucus_basla(self):
        if self.dron_pil == 100:
            print(f'uçus için uygundur piliniz {self.dron_pil}')
        else :
            print(f'ucuş için pil {self.dron_pil} durumu uygun değildir')
            vakit=100-int(self.dron_pil)
            for i in range(vakit):
                self.dron_pil += 1
                time.sleep(0.2)
                if self.dron_pil <= 100:
                    print(f'dron pili %{self.dron_pil} dolu durumda')
                    self.ui.pro_batarya.setValue(self.dron_pil) 
                else:
                     print(f'dron pili %{self.dron_pil} dolu durumda')  
                     
    def ucus_durdur(self):
        print(f'{self.id }ucus iptal ediliyor')

class yeni_dron():
    def __init__(self):
        self.kullanici=[]

    def yeni_kullanici(self,veri):
        self.kullanici.append(veri)  


