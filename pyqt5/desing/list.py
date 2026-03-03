import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QListWidget,QMainWindow,QListWidget, QListWidgetItem, QVBoxLayout, QWidget,QInputDialog
from listui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadStudents()
        self.ui.btn_add.clicked.connect(self.addStudent)
        self.ui.btn_edit.clicked.connect(self.editStudent)
        self.ui.btn_remove.clicked.connect(self.removeStudent)
        self.ui.btn_up.clicked.connect(self.moveUp)
        self.ui.btn_down.clicked.connect(self.moveDown)
        self.ui.btn_sort.clicked.connect(self.sortItems)
        self.ui.btn_exit.clicked.connect(self.close)

    def loadStudents(self):
        students = ['Ali','Veli','Ayşe','Fatma','Ahmet']
        self.ui.listWidget.addItems(students)    

    def addStudent(self):
        text, ok = QInputDialog.getText(self, "Add Student", "Enter student name:")
        if ok and text:
            self.ui.listWidget.addItem(text)

    def editStudent(self):
        current_item = self.ui.listWidget.currentItem()
        if current_item:
            text, ok = QInputDialog.getText(self, "Edit Student", "Enter new name:", text=current_item.text())
            if ok:
                current_item.setText(text)
   
    def removeStudent(self):
        current_row = self.ui.listWidget.currentRow()
        if current_row >= 0:
            self.ui.listWidget.takeItem(current_row)

    def moveUp(self):
        current_row = self.ui.listWidget.currentRow()
        if current_row > 0:
            current_item = self.ui.listWidget.takeItem(current_row)
            self.ui.listWidget.insertItem(current_row - 1, current_item)
            self.ui.listWidget.setCurrentRow(current_row - 1)

    def moveDown(self):
        current_row = self.ui.listWidget.currentRow()
        if current_row < self.ui.listWidget.count() - 1:
            current_item = self.ui.listWidget.takeItem(current_row)
            self.ui.listWidget.insertItem(current_row + 1, current_item)
            self.ui.listWidget.setCurrentRow(current_row + 1)

    def sortItems(self):
        self.ui.listWidget.sortItems()

    def close(self):
        QtWidgets.QApplication.quit()                            


def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()            