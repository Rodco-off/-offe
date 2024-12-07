from sys import argv, exit
from sqlite3 import connect

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView


class CoffeeBaseDate(QMainWindow):

    BASE_DATA = 'coffee.sqlite'

    def __init__(self) -> None:

        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

        self.show_table: QPushButton
        self.table: QTableWidget

    def initUI(self) -> None:

        self.show_table.clicked.connect(self.click_show_table)
        self.show_table.click()

    def update_table(self) -> None:

        self.table.clear()

        self.table.setColumnCount(7)
        self.table.setRowCount(0)
        result = self.get_result_table()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.setHorizontalHeaderLabels(('ID', 'название сорта', 'степень обжарки', 'молотый/в зернах', 'описание вкуса', 'цена', 'объем упаковки'))

        for i, row in enumerate(result):

            self.table.setRowCount(self.table.rowCount() + 1)

            for j, elem in enumerate(row):

                self.table.setItem(i, j, QTableWidgetItem(str(elem)))

    def get_result_table(self) -> tuple[list]:

        with connect(self.BASE_DATA) as con:

            cursor = con.cursor()
            result = cursor.execute('''SELECT * FROM Coffee''')

        return result

    def click_show_table(self) -> None:

        self.update_table()


if __name__ == '__main__':

    app = QApplication(argv)
    coffee = CoffeeBaseDate()
    coffee.show()
    exit(app.exec())
