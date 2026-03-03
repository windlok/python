import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QDateEdit,QMainWindow,QWidget, QDateTimeEdit, QVBoxLayout
from PyQt5.QtCore import QDate, QTime, QDateTime
from time_editui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_calculator.clicked.connect(self.calculate)

    def calculate(self):
        start=self.ui.date_start.date()
        end=self.ui.date_end.date()
        print(f'start: {start} ,end: {end}') 
        print('Days is month: {}'.format(start.daysInMonth())) 
        print('Days is year: {}'.format(start.daysInYear()))

        print('total days: {}'.format(start.daysTo(end))) 
        
        now = QDate.currentDate()

        print('total days to now: {}'.format(start.daysTo(now)))


def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_()) 

app() 

