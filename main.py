import sys
from PyQt5 import uic
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute("""SELECT name FROM coffee""").fetchall()
        for elem in result:
            self.comboBox.addItem(*elem)
        con.close()
        self.do_paint = False
        self.first = False
        self.pushButton.clicked.connect(self.find)

    def find(self):
        name = self.comboBox.currentText()
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        text = self.lineEdit.text()
        result = cur.execute(f"""SELECT * FROM coffee
                                        WHERE name like '{name}'""").fetchall()
        self.lineEdit.setText(str(result[0][0]))
        self.lineEdit_2.setText(str(result[0][2]))
        self.lineEdit_3.setText(str(result[0][3]))
        self.lineEdit_4.setText(str(result[0][4]))
        self.lineEdit_5.setText(str(result[0][5]))
        self.lineEdit_6.setText(str(result[0][6]))
        self.lineEdit_7.setText(str(result[0][7]))
        con.close()




def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Example()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())