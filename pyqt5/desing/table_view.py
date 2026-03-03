import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QListWidget,QMainWindow, QTableWidgetItem,QWidget, QVBoxLayout
from table_viewui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.loadProducts()

    def saveProducts(self):
        name =self.txtName.text()
        model = self.txtModel.text()

        if name and model:
            new_product = {"id": len(self.products) + 1, "name": name, "model": model}
            self.products.append(new_product)
            self.tableWidget.setRowCount(len(self.products))
            self.tableWidget.setItem(len(self.products) - 1, 0, QTableWidgetItem(str(new_product["id"])))
            self.tableWidget.setItem(len(self.products) - 1, 1, QTableWidgetItem(new_product["name"]))
            self.tableWidget.setItem(len(self.products) - 1, 2, QTableWidgetItem(new_product["model"]))
            self.txtName.clear()
            self.txtModel.clear()

    def loadProducts(self):
        self.products= [
            {"id": 1, "name": "samsung", "model": "a3"},
            {"id": 2, "name": "apple", "model": "iphone12"},
            {"id": 3, "name": "huawei", "model": "p30"},
            {"id": 4, "name": "xiaomi", "model": "redmi note 9"},
            {"id": 5, "name": "lg", "model": "g6"},
            {"id": 6, "name": "asus", "model": "zenfone 5"},
        ]
        self.tableWidget.setRowCount(len(self.products))
        self.tableWidget.setColumnCount(3)
        self.setHeaderLabels = ["id", "name", "model"]
        self.tableWidget.setHorizontalHeaderLabels(self.setHeaderLabels)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        for i, product in enumerate(self.products):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(product["id"])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(product["name"]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(product["model"]))



def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()