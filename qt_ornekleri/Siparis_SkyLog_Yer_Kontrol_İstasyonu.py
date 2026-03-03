import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow , QToolTip
from skylogui import Ui_MainWindow
from dron import dron
import random
# remove global drone instance; will be created after UI is ready

class App(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # create drone with a reference to the UI so it can update widgets
        self.d = dron("dji", 12, ui=self.ui)  # Pil sadece %10

        self.ui.sistemi_baslat.clicked.connect(self.d.ucus_basla)
        self.ui.sistemi_durdur.clicked.connect(self.d.ucus_durdur)
        

        
application = QtWidgets.QApplication(sys.argv)
window =App()
window.show()
sys.exit(application.exec_())