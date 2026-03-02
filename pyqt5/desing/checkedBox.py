import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from checkedBoxui import Ui_MainWindow

class CheckedBox(QMainWindow):
    def __init__(self):
        super(CheckedBox, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_secilen.clicked.connect(self.getAllChecked)

        self.ui.cb_sinema.stateChanged.connect(self.show_state)
        self.ui.cb_kitap_2.stateChanged.connect(self.show_state)
        self.ui.cb_spor.stateChanged.connect(self.show_state)
        self.ui.cb_bos.stateChanged.connect(self.show_state)

    def show_state(self,value):
        sender = self.sender()
        if sender.isChecked():
            print(f'{sender.text()} seçildi')
        else:
            print(f'{sender.text()} seçilmedi')
    
    def getAllChecked(self):
        # findChildren() fonksiyonu, belirli bir türdeki tüm alt widget'ları bulmak için kullanılır.
        result =''
        items = self.ui.grouphobi.findChildren(QtWidgets.QCheckBox)
        for item in items:
            if item.isChecked():
                result += item.text() + ' \n'
            self.ui.lbl_text.setText(result)
        items2 = self.ui.groupders.findChildren(QtWidgets.QCheckBox)
        for item in items2:
            if item.isChecked():
                result += item.text() + ' \n'
            self.ui.lbl_text.setText(result)    
def app():
    app = QApplication(sys.argv)
    win = CheckedBox()
    win.show()
    sys.exit(app.exec_())

app()            