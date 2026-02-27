import random
from time import time
import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow , QToolTip
from MainWindow import Ui_MainWindow


class dron():
    def __init__(self,ad,pil, ui=None):
        self.id = 0
        self.dron_adi = ad
        self.dron_pil = pil
        self.dron_kilo = 0
        self.dron_aktif = "evet"
        # ui reference may be provided later
        self.ui = ui
        self.dron_max_kilo = 10

    def yuk_al(self,gelen_kilo):
        self.dron_mevcut_kilo = gelen_kilo
        if self.dron_mevcut_kilo <= self.dron_max_kilo:
            print(f'uçus için uygundur {self.dron_mevcut_kilo} kilo tasimak icin uygundur')
        else:
            print(f'yuk {self.dron_kilo} üstünde')

    def ucus_basla(self):
        sayi=[]
        if self.dron_pil == 100:
            print(f'uçus için uygundur piliniz {self.dron_pil}')
            for i in range(50):
                sayi.append(random.randint(1,5000))
                time.sleep(0.8)
                self.ui.lbl_irtifa.insertPlainText(str(sayi[i])+"\n")
        else :
            print(f'ucuş için pil {self.dron_pil} durumu uygun değildir')
            vakit=100-int(self.dron_pil)
            for i in range(vakit+1):
                self.dron_pil += 1
                time.sleep(0.1)
                if self.dron_pil <= 100:
                    self.ui.pro_batarya.setValue(self.dron_pil) 
                else:
                    print(f'dron pili %{self.dron_pil-1} dolu durumda') 
                    self.ui.l_dronid.setText('Dron Ucmaya Hazır ')
                    for i in range(50):
                        if self.ui.sistemi_baslat.clicked:
                            sayi.append(random.randint(1,5000)),
                            time.sleep(0.5)
                            self.ui.lbl_irtifa.insertPlainText(str(sayi[i])+"\n")
                            if self.dron_pil <= 25:
                                print(f'pil bitiyor')
                                break
                            else:
                                self.dron_pil -= 1
                                self.ui.pro_batarya.setValue(self.dron_pil) 
    
            
                
                     
    def ucus_durdur(self):
        print(f'{self.id }ucus iptal ediliyor')

class yeni_dron():
    def __init__(self):
        self.kullanici=[]

    def yeni_kullanici(self,veri):
        self.kullanici.append(veri)  


