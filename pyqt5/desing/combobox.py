import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow
from comboboxui import Ui_MainWindow

class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows,self).__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #addItems combobox içine verileri yüklemek için kullanılır
        # self.ui.cbsehirler.addItem('ankara')
        # self.ui.cbsehirler.addItem('istanbul')
        # self.ui.cbsehirler.addItem('izmir')
        # self.ui.cbsehirler.addItem('afyon')
        #self.ui.cbsehirler.addItems(['ankara','istanbul','afyon'])
        self.ui.btn_load.clicked.connect(self.LoadItems)
        self.ui.btn_get.clicked.connect(self.GetItems)
        self.ui.btn_clear.clicked.connect(self.Clear)
        #secilen yerin indexsini 
        self.ui.cbsehirler.currentIndexChanged.connect(self.selectedChangindex)
        #secilen yerin adını verir
        self.ui.cbsehirler.currentIndexChanged[str].connect(self.selectedChangtext)
        

    def LoadItems(self):
        sehirler= ['ankara','istanbul','afyon']
        self.ui.cbsehirler.addItems(sehirler)

    def GetItems(self):
        result=self.ui.cbsehirler.currentText()
        print(f'gelen veri {result}')
        print(self.ui.cbsehirler.currentIndex())
        print(self.ui.cbsehirler.count())

    def selectedChangindex(self,index):
        print(index)

    def selectedChangtext(self,text):
        print(text)

    def Clear(self):
        print('veriler temizlendi')
        self.ui.cbsehirler.clear()

def app():
    app = QApplication(sys.argv)
    win = MainWindows()
    win.show()
    sys.exit(app.exec_())

app()