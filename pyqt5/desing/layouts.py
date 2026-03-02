import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QPushButton, QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        #setAutoFillBackground(True) parametresi, widget'in arka plan rengini doldurmak için kullanılır. 
        # Bu, widget'in arka plan renginin görünür olmasını sağlar. 
        # Eğer bu parametre False olarak ayarlanırsa, widget'in arka plan rengi doldurulmaz ve varsayılan olarak saydam olur.
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layouts")
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and set it as the central widget of the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # QvBoxLayout, widget'leri dikey olarak düzenlemek için kullanılır.
        # QHBoxLayout, widget'leri yatay olarak düzenlemek için kullanılır.
        # QGridLayout, widget'leri ızgara şeklinde düzenlemek için kullanılır
        layout = QGridLayout()
        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("orange"), 1, 0)
        layout.addWidget(Color("red"), 1, 1)
        layout.addWidget(Color("blue"), 1, 2)
        layout.addWidget(Color("red"), 2, 0)
        layout.setContentsMargins(30, 10, 50, 50) # layout'un kenar boşluklarını sıfırlamak için kullanılır.

        layout1 = QVBoxLayout()
        layout1.addWidget(Color("red"))
        layout1.addWidget(Color("blue"))
        layout1.addWidget(Color("green"))
        layout1.setContentsMargins(0, 0, 60, 10) # layout'un kenar boşluklarını sıfırlamak için kullanılır.

        layout2 = QHBoxLayout()
        layout2.addWidget(Color("red"))
        layout2.addWidget(Color("blue"))
        layout2.addWidget(Color("green"))


        vlayout = QHBoxLayout()
        vlayout.addLayout(layout)
        vlayout.addLayout(layout1)
        vlayout.addLayout(layout2)
        



        # Set the layout for the central widget
        central_widget.setLayout(vlayout)

def app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

app()