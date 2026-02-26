from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class App(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.toplama)
        self.ui.pushButton_2.clicked.connect(self.cikartma)
        self.ui.pushButton_3.clicked.connect(self.bolme)
        self.ui.pushButton_4.clicked.connect(self.carpma)

    def toplama(self):
        sayi1 = int(self.ui.txt_sayi1.text())
        sayi2 = int(self.ui.txt_sayi2.text())
        sonuc = sayi1 + sayi2
        self.ui.lbl_sonuc.setText(str(sonuc))

    def cikartma(self):
        sayi1 = int(self.ui.txt_sayi1.text())
        sayi2 = int(self.ui.txt_sayi2.text())
        sonuc = sayi1 - sayi2
        self.ui.lbl_sonuc.setText(str(sonuc))

    def bolme(self):
        sayi1 = int(self.ui.txt_sayi1.text())
        sayi2 = int(self.ui.txt_sayi2.text())
        sonuc = sayi1 / sayi2
        self.ui.lbl_sonuc.setText(str(sonuc))

    def carpma(self):
        sayi1 = int(self.ui.txt_sayi1.text())
        sayi2 = int(self.ui.txt_sayi2.text())
        sonuc = sayi1 * sayi2
        self.ui.lbl_sonuc.setText(str(sonuc))

application = QtWidgets.QApplication(sys.argv)
window = App()
window.show()
sys.exit(application.exec_())        