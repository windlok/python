import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow , QToolTip
from MainWindow import Ui_MainWindow
from dron import dron
import random
d=dron("dji",10)

class App(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.sistemi_baslat.clicked.connect(
            lambda: (d.ucus_basla, self.baslat())
        )
        self.ui.sistemi_durdur.clicked.connect(d.ucus_durdur)

    def baslat(self):
        sayi=[]
        for i in range(50):
            sayi.append(random.randint(1,5000))
            time.sleep(0.8)
            self.ui.lbl_irtifa.insertPlainText(str(sayi[i])+"\n")

    def durdur(self):
        d.ucus_durdur()
        
application = QtWidgets.QApplication(sys.argv)
window =App()
window.show()
sys.exit(application.exec_())