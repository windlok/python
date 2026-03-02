import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainFrom(QMainWindow):
    def __init__(self):
        super(MainFrom, self).__init__()
        self.setWindowTitle('Calculator')
        self.setGeometry(200, 200, 500, 500)
        self.initUI()

    def initUI(self):
        self.lbl_sayi1 = QtWidgets.QLabel(self)
        self.lbl_sayi1.setText('Sayi 1: ')
        self.lbl_sayi1.move(50, 30)

        self.txt_sayi1 = QtWidgets.QLineEdit(self)
        self.txt_sayi1.move(150, 30)

        self.lbl_sayi2 = QtWidgets.QLabel(self)
        self.lbl_sayi2.setText('Sayi 2: ')
        self.lbl_sayi2.move(50, 80)

        self.txt_sayi2 = QtWidgets.QLineEdit(self)
        self.txt_sayi2.move(150, 80)

        self.btn_topla = QtWidgets.QPushButton(self)
        self.btn_topla.setText('Topla')
        self.btn_topla.move(45, 130)
        self.btn_topla.clicked.connect(self.hesapla)

        self.btn_cikart = QtWidgets.QPushButton(self)
        self.btn_cikart.setText('Cikart')
        self.btn_cikart.move(150, 130)
        self.btn_cikart.clicked.connect(self.hesapla)

        self.btn_carp = QtWidgets.QPushButton(self)
        self.btn_carp.setText('Carp')
        self.btn_carp.move(45, 180)
        self.btn_carp.clicked.connect(self.hesapla)

        self.btn_bol = QtWidgets.QPushButton(self)
        self.btn_bol.setText('Bol')
        self.btn_bol.move(150, 180)
        self.btn_bol.clicked.connect(self.hesapla)

        self.lbl_sonuc = QtWidgets.QLineEdit(self)
        self.lbl_sonuc.move(320, 100)

    def hesapla(self):
        sender = self.sender()
        result = 0
        if sender.text() == "Topla":
            result = int(self.txt_sayi1.text()) + int(self.txt_sayi2.text())
        elif sender.text() == "Cikart":
            result = int(self.txt_sayi1.text()) - int(self.txt_sayi2.text())
        elif sender.text() == "Carp":
            result = int(self.txt_sayi1.text()) * int(self.txt_sayi2.text())
        elif sender.text() == "Bol":
            result = int(self.txt_sayi1.text()) / int(self.txt_sayi2.text())
        self.lbl_sonuc.setText('sonuc: ' + str(result))        
        

def app():
    app = QApplication(sys.argv)
    win = MainFrom()
    win.show()
    sys.exit(app.exec())

app()
