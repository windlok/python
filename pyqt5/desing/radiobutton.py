import sys 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from radioboxui import Ui_MainWindow

class MainFrom(QMainWindow):
    def __init__(self):
        super(MainFrom, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #setchecked() fonksiyonu, bir radio button'un seçili olup olmadığını belirlemek için kullanılır. 
        # Eğer parametre olarak True verilirse, radio button seçili hale gelir; False verilirse, radio button seçili olmaz.
        # self.ui.radio_18_24.setChecked(True)
        
        # toggled sinyali, bir radio button'un durumunun değiştiğinde tetiklenen bir sinyaldir.
        self.ui.radio_turk.toggled.connect(self.on_radio_button_toggled)
        self.ui.radip_azer.toggled.connect(self.on_radio_button_toggled)
        self.ui.radio_alman.toggled.connect(self.on_radio_button_toggled)
        self.ui.radi_yun.toggled.connect(self.on_radio_button_toggled)

        self.ui.radio_ilk.toggled.connect(self.on_radio_button_toggled_egitim)
        self.ui.radio_lise.toggled.connect(self.on_radio_button_toggled_egitim)
        self.ui.radio_ni.toggled.connect(self.on_radio_button_toggled_egitim)
        self.ui.radio_yuk.toggled.connect(self.on_radio_button_toggled_egitim)

        self.ui.radio_18_24.toggled.connect(self.on_radio_button_toggled_yas)
        self.ui.radio_24_30.toggled.connect(self.on_radio_button_toggled_yas)
        self.ui.radio_30_45.toggled.connect(self.on_radio_button_toggled_yas)
        self.ui.radio_45ust.toggled.connect(self.on_radio_button_toggled_yas)
        self.ui.pushButton.clicked.connect(self.getSelectedulke)
        self.ui.pushButton_2.clicked.connect(self.getSelectedEgitim)
        self.ui.pushButton_3.clicked.connect(self.getSelectedYas)

        
    def on_radio_button_toggled(self):
        sender = self.sender()
        if sender.isChecked():
            self.ui.lbl_ulke.setText(f'{sender.text()} seçildi')

    def on_radio_button_toggled_egitim(self):
        sender = self.sender()
        if sender.isChecked():
            self.ui.lbl_egitim.setText(f'{sender.text()} seçildi')

    def on_radio_button_toggled_yas(self):
        sender = self.sender()
        if sender.isChecked():
            self.ui.lbl_yas.setText(f'{sender.text()} seçildi')

    def getSelectedulke(self):
        items = self.ui.groupBox_ulke.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_ulke.setText(f'Seçilen ülke: {rb.text()}')
    
    def getSelectedEgitim(self):
        items = self.ui.groupBox_egitim.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_egitim.setText(f'Seçilen eğitim: {rb.text()}')

    def getSelectedYas(self):
        items = self.ui.groupBox_yas.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_yas.setText(f'Seçilen yaş: {rb.text()}')
    


def app():
    app = QApplication(sys.argv)
    win = MainFrom()
    win.show()
    sys.exit(app.exec_())

app()