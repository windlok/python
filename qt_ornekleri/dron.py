import random
import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow , QToolTip
from skylogui import Ui_MainWindow


class dron(QMainWindow):
    def __init__(self,ad,pil, ui=None):
        super(dron,self).__init__()
        self.id = 0
        self.dron_adi = ad
        self.dron_pil = pil
        self.dron_kilo = 0
        self.dron_aktif = "evet"
        # ui reference may be provided later
        self.ui = ui
        self.dron_max_kilo = 10
        
        # Timer'lar için değişkenler
        self.sarj_timer = QTimer()
        self.ucus_timer = QTimer()
        self.irtifa_sayaci = 0
        self.sarj_timer.timeout.connect(self.sarj_et)
        self.ucus_timer.timeout.connect(self.ucus_guncelle)

    def yuk_al(self,gelen_kilo):
        self.dron_mevcut_kilo = gelen_kilo
        if self.dron_mevcut_kilo <= self.dron_max_kilo:
            print(f'uçus için uygundur {self.dron_mevcut_kilo} kilo tasimak icin uygundur')
        else:
            print(f'yuk {self.dron_kilo} üstünde')

    def ucus_basla(self):
        if self.dron_pil <= 20:
            print(f'Uçuş için uygundur, piliniz %{self.dron_pil}')
            self.ui.l_dronid.setText('Uçuş Başladı')
            self.irtifa_sayaci = 0
            self.ucus_timer.start(800)  # Her 800ms'de bir güncelle
            self.dron_bilgileri()
        else:
            print(f'Uçuş için pil %{self.dron_pil} durumu uygun değildir, şarj başlatılıyor...')
            self.ui.l_dronid.setText('Şarj Ediliyor...')
            self.sarj_timer.start(100)  # Her 100ms'de bir şarj et
    
    def sarj_et(self):
        if self.dron_pil < 100:
            self.dron_pil += 1
            self.ui.pro_batarya.setValue(self.dron_pil)
        else:
            self.sarj_timer.stop()
            print(f'Dron pili %{self.dron_pil} dolu durumda')
            self.ui.l_dronid.setText('Dron Uçmaya Hazır')
            # Şarj tamamlandı, otomatik uçuş başlat
            self.irtifa_sayaci = 0
            self.ucus_timer.start(500)
    
    def ucus_guncelle(self):
        if self.irtifa_sayaci < 50 and self.dron_pil > 25:
            irtifa = random.randint(1, 5000)
            self.ui.lbl_irtifa.insertPlainText(str(irtifa) + "\n")
            self.dron_pil -= 1
            self.ui.pro_batarya.setValue(self.dron_pil)
            self.irtifa_sayaci += 1
        else:
            self.ucus_timer.stop()
            if self.dron_pil <= 25:
                print(f'Pil bitiyor, uçuş sonlandırılıyor')
                self.ui.l_dronid.setText('Pil Bitti')
            else:
                print(f'Uçuş tamamlandı')
                self.ui.l_dronid.setText('Uçuş Tamamlandı') 
    
                     
    def ucus_durdur(self):
        self.sarj_timer.stop()
        self.ucus_timer.stop()
        print(f'{self.id} uçuş iptal ediliyor')
        self.ui.l_dronid.setText('Sistem Durduruldu')

    def dron_bilgileri(self):
        self.ui.lbl_dronadi.setText(self.dron_adi)
        self.ui.lbl_dronkilo.setText(str(self.dron_kilo))
        self.ui.lbl_dronpil.setText(str(self.dron_pil))  


