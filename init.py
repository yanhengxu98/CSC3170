from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#from PyQt5.QtSql import QSqlDatabase, QsqlTableModel

import sys
import pymysql

from database_project import Ui_Form


class MyMainwindow(QMainWindow, Ui_Form):

    def __init__(self, parent = None):
        super(MyMainwindow, self).__init__(parent)
        self.setupUi(self)
        self.connection = pymysql.connect(host='10.26.1.10', user='root', password='root', db='LGUAirline', port=3306,
                                          charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        self.prefix = "select * from flight where DepApFCC = SZX"

    # def query(self):


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = MyMainwindow()
    ui.show()
    sys.exit(app.exec_())


