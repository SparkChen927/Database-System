from InterfaceUi import *
from LoginUi import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
import pymysql

# db = pymysql.connect(
#     host='localhost',
#     port=3306,
#     user="root",
#     password='',
#     database='purchase',
#     charset='utf8'
# )


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_in.clicked.connect(self.go_to_main)
        self.ui.pushButton_up.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_r.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_in.clicked.connect(self.sign_up)
        self.show()

    def go_to_main(self):
        account = self.ui.lineEdit_u.text()
        password = self.ui.lineEdit_p.text()
        if account == "admin" and password == "123456":
            InterfaceWindow()
            self.close()
        else:
            QMessageBox.critical(self, "错误", "账号或密码错误")

    def sign_up(self):
        account = self.ui.lineEdit_u2.text()
        password = self.ui.lineEdit_p2.text()

    # 拖动
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


class InterfaceWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_sup.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_app.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_buy.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.pushButton_anly.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_doc.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.pushButton_exit.clicked.connect(self.back_to_login)
        self.ui.pushButton_maxsize.clicked.connect(self.resize_win)  # 注意不要有括号
        self.show()

    def back_to_login(self):
        LoginWindow()
        self.close()

    def resize_win(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_maxsize.setIcon(QtGui.QIcon(":/icons/icons/maxmize.png"))
            self.ui.tableWidget_sup.horizontalHeader().setStretchLastSection(False)
            self.ui.tableWidget_sup.verticalHeader().setStretchLastSection(False)
            self.ui.tableWidget_app.horizontalHeader().setStretchLastSection(False)
            self.ui.tableWidget_app.verticalHeader().setStretchLastSection(False)
            self.ui.tableWidget_buy.horizontalHeader().setStretchLastSection(False)
            self.ui.tableWidget_buy.verticalHeader().setStretchLastSection(False)
            self.ui.tableWidget_doc.horizontalHeader().setStretchLastSection(False)
            self.ui.tableWidget_doc.verticalHeader().setStretchLastSection(False)
            self.ui.tableWidget_anly.horizontalHeader().setStretchLastSection(False)
            self.ui.tableWidget_anly.verticalHeader().setStretchLastSection(False)
        else:
            self.showMaximized()
            self.ui.pushButton_maxsize.setIcon(QtGui.QIcon(":/icons/icons/minisize.png"))
            self.ui.tableWidget_sup.horizontalHeader().setStretchLastSection(True)
            self.ui.tableWidget_sup.verticalHeader().setStretchLastSection(True)
            self.ui.tableWidget_app.horizontalHeader().setStretchLastSection(True)
            self.ui.tableWidget_app.verticalHeader().setStretchLastSection(True)
            self.ui.tableWidget_buy.horizontalHeader().setStretchLastSection(True)
            self.ui.tableWidget_buy.verticalHeader().setStretchLastSection(True)
            self.ui.tableWidget_doc.horizontalHeader().setStretchLastSection(True)
            self.ui.tableWidget_doc.verticalHeader().setStretchLastSection(True)
            self.ui.tableWidget_anly.horizontalHeader().setStretchLastSection(True)
            self.ui.tableWidget_anly.verticalHeader().setStretchLastSection(True)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())
