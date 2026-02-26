import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

# MyWindow sınıfı, QMainWindow sınıfından türetilmiş bir sınıftır. 
# Bu sınıf, PyQt5 uygulamasında kullanılacak ana pencereyi temsil eder.
class MyWindow(QMainWindow):
    # __init__() metodu, MyWindow sınıfının yapıcı (constructor) metodudur. 
    # Bu metod, MyWindow sınıfından bir nesne oluşturulduğunda otomatik olarak çağrılır ve pencerenin temel özelliklerini ayarlar.
    def __init__(self):
        # super() fonksiyonu, MyWindow sınıfının üst sınıfı olan QMainWindow'un __init__() metodunu çağırmak için kullanılır. 
        # Bu, QMainWindow'un temel özelliklerini ve işlevselliğini MyWindow sınıfına dahil eder.
        super(MyWindow, self).__init__()

        self.setWindowTitle("PyQt5 App")
        self.setGeometry(200, 200, 300, 200)
        self.setWindowIcon(QIcon('icon.png'))
        self.setToolTip('bekleyin...')
        # bunu yaparak, MyWindow sınıfının __init__() metodunda initui() metodunu çağırarak kullanıcı arayüzünü oluşturur ve düzenleriz. 
        # Bu sayede, MyWindow sınıfından bir nesne oluşturulduğunda, initui() metodu otomatik olarak çalışır ve pencereye gerekli widget'lar eklenir.
        self.initui()
# initui() metodu, MyWindow sınıfının kullanıcı arayüzünü oluşturmak ve düzenlemek için kullanılan bir metoddur. 
# Bu metod, pencereye çeşitli widget'lar ekler ve bu widget'ların özelliklerini ayarlar.
    def initui(self):
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("ADİNİZ:")
        self.lbl_name.move(50, 20)
        

        self.lbl2_surname = QtWidgets.QLabel(self)
        self.lbl2_surname.setText("SOYADINIZ:")
        self.lbl2_surname.move(50, 60)

        self.lbl_resut = QtWidgets.QLabel(self)
        self.lbl_resut.resize(160, 20)
        self.lbl_resut.move(100, 140)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(120, 20)
        self.txt_name.resize(150, 20)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(120,60)
        self.txt_surname.resize(150, 20)

        def clicked():
            self.lbl_resut.setText(f'Adınız: {self.txt_name.text()} Soyadınız: {self.txt_surname.text()}')

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("kaydet")
        self.btn_save.move(120,100)
        self.btn_save.clicked.connect(clicked)
        


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


    win.show()
    sys.exit(app.exec_())

window()