import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

# clicked() fonksiyonu, QPushButton widget'ına tıklandığında çağrılacak bir işlevdir. 
# Bu fonksiyon, butona tıklandığında "butona tıklandı" mesajını konsola yazdırır.

    
def window():
    app = QApplication(sys.argv)
    win = QWidget()
    win = QMainWindow()

    win.setWindowTitle("PyQt5 App")
    win.setGeometry(200, 200, 300, 200)
    win.setWindowIcon(QIcon('icon.png'))
    win.setToolTip('bekleyin...')

# QLabel, PyQt5'te metin veya görüntü gibi içerikleri göstermek için kullanılan bir widget sınıfıdır. 
# QLabel, genellikle kullanıcı arayüzünde statik metin veya resim göstermek için kullanılır.
    lbl = QtWidgets.QLabel(win)
    lbl.setText("ADİNİZ:")
    lbl.move(50, 20)
    
    lbl2 = QtWidgets.QLabel(win)
    lbl2.setText("SOYADINIZ:")
    lbl2.move(50, 60)

# QLineEdit, PyQt5'te kullanıcıdan metin girişi almak için kullanılan bir widget sınıfıdır.
    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(120, 20)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(120,60)

    def clicked(self):
            print(f'butona tıklandı. Adınız: {txt_name.text()} Soyadınız: {txt_surname.text()}')

# QPushButton, PyQt5'te bir düğme oluşturmak için kullanılan bir widget sınıfıdır. QPushButton, kullanıcıların tıklayarak belirli bir işlemi gerçekleştirmesini sağlar.
    btn_save= QtWidgets.QPushButton(win)
    btn_save.setText("kaydet")
    btn_save.move(120,100)
    # clicked() fonksiyonunu QPushButton widget'ının clicked sinyaline bağlar. 
    # Bu, butona tıklandığında clicked() fonksiyonunun çağrılmasını sağlar.
    btn_save.clicked.connect(clicked)
    
    

    win.show()
    sys.exit(app.exec_())

window()