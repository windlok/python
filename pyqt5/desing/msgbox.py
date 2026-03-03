import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox
from msgboxui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()

        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.btn_exit.clicked.connect(self.showDialog)

    def showDialog(self):
        #tek satırda bütün işlemi yaparız
        result = QMessageBox.question(self,'close application','are you sure',QMessageBox.Ok | QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print("yes clicked")
            QtWidgets.qApp.quit()
        else:
            print("sagolasın adammımm")    


    #     self.msg = QMessageBox(self)
    #     self.msg.setText("are you sure")
    #     self.msg.setWindowTitle('close application')
    #     self.msg.setIcon(QMessageBox.Warning)
    #     self.msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    #     self.msg.buttonClicked.connect(self.popup_button)
    #     self.msg.exec_()

    # def popup_button(self, button):
    #     if self.msg.standardButton(button) == QMessageBox.Ok:
    #         QtWidgets.qApp.quit()
    #     else:
    #         print('cancel...')        
def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()