from PyQt5.QtGui import QBrush, QColor
from InterfaceUi import *
from LoginUi import *
from UpdateUi import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
import sys
import pymysql

db = pymysql.connect(
    host='localhost',
    port=3306,
    user="root",
    password='',
    database='purchase',
    charset='utf8'
)


a = 0
def coo(num):
    global a
    a = num
    return a


gname = ""
def gname_f(str):
    global gname
    gname = str
    return gname


gno_g = ""
def gno_f(str):
    global gno_g
    gno_g = str
    return gno_g


sname = ""
def sname_f(str):
    global sname_i
    sname_i = str
    return sname_i


ano = ""
def ano_f(str):
    global ano
    ano = str
    return ano


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.pushButton_in.clicked.connect(self.login_in)
        self.ui.pushButton_up.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.pushButton_r.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.pushButton_u.clicked.connect(self.sign_up)
        self.show()

    def login_in(self):
        cursor = db.cursor()
        account = self.ui.lineEdit_u.text()
        password = self.ui.lineEdit_p.text()
        sql = "select * from users where username = '%s' and password = '%s'" % (account, password)
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        if cursor.fetchone() is None:
            QMessageBox.critical(self, "错误", "账号或密码错误")
        else:
            InterfaceWindow().ui.stackedWidget.setCurrentIndex(0)
            self.close()
        cursor.close()

    def sign_up(self):
        self.ui.lineEdit_u.setText("")
        self.ui.lineEdit_p.setText("")
        cursor = db.cursor()
        account = self.ui.lineEdit_u2.text()
        password = self.ui.lineEdit_p2.text()
        sql = "select * from users where username = '%s'" % account
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        if cursor.fetchone() is None:
            sql = "insert into users values ('%s', '%s')" % (account, password)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            QMessageBox.information(self, "消息", "注册成功")
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.lineEdit_u.setText(account)
            self.ui.lineEdit_p.setText(password)
            self.ui.lineEdit_u2.setText("")
            self.ui.lineEdit_p2.setText("")
        else:
            QMessageBox.critical(self, "错误", "账号已存在")
            self.ui.lineEdit_u2.setText("")
            self.ui.lineEdit_p2.setText("")
        db.commit()
        cursor.close()

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

        self.init_sup()
        self.ui.pushButton_sup.clicked.connect(self.go_to_sup)
        self.ui.pushButton_supEdit.clicked.connect(self.go_to_edit)
        self.ui.pushButton_supAdd.clicked.connect(self.add_sup)
        self.ui.pushButton_supFind.clicked.connect(self.find_sup)

        self.ui.pushButton_app.clicked.connect(self.go_to_app)
        self.ui.pushButton_appAdd.clicked.connect(self.add_app)
        self.ui.pushButton_appFind.clicked.connect(self.find_app)

        self.ui.pushButton_buy.clicked.connect(self.go_to_buy)
        self.ui.pushButton_buyFind.clicked.connect(self.find_buy)

        self.ui.pushButton_doc.clicked.connect(self.go_to_doc)
        self.ui.pushButton_doc.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.pushButton_anlyFind.clicked.connect(self.find_doc)

        self.ui.pushButton_anly.clicked.connect(self.go_to_anly)
        self.ui.pushButton_docFind.clicked.connect(self.find_anly)

        self.ui.pushButton_editAdd.clicked.connect(self.add_edit)
        self.ui.pushButton_editFind.clicked.connect(self.find_edit)

        self.ui.pushButton_exit.clicked.connect(self.back_to_login)
        self.ui.pushButton_maxsize.clicked.connect(self.resize_win)  # 注意不要有括号
        self.show()

    def back_to_login(self):
        LoginWindow()
        self.close()

    def go_to_edit(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.init_edit()

    def init_edit(self):
        cursor = db.cursor()
        sql = "select sname, type, address, settlement, credit from suppliers"
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        result = list(result)
        if result:
            row = cursor.rowcount
            self.ui.tableWidget_edit.setRowCount(row)
            for i in range(len(result)):
                result[i] = list(result[i])
            for i in range(row):
                self.ui.tableWidget_edit.setCellWidget(i, 5, self.button_edit())
                for j in range(5):
                    if result[i][j] is not None:
                        item = QTableWidgetItem(str(result[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_edit.setItem(i, j, item)
        else:
            self.ui.tableWidget_edit.setRowCount(0)
        cursor.close()

    def button_edit(self):
        widget = QtWidgets.QWidget()
        # 修改
        self.updateBtn = QtWidgets.QPushButton('编辑')
        self.updateBtn.setStyleSheet(''' text-align : center;
                                                  background-color : NavajoWhite;
                                                  height : 30px;
                                                  border-style: outset;
                                                  font : 13px  ''')
        self.updateBtn.clicked.connect(self.update_edit)

        # 删除
        self.deleteBtn = QtWidgets.QPushButton('删除')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                            background-color : LightCoral;
                                            height : 30px;
                                            border-style: outset;
                                            font : 13px; ''')
        self.deleteBtn.clicked.connect(self.delete_edit)

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.updateBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def add_edit(self):
        coo(2)
        UpdateDlg().exec_()
        self.init_edit()

    def update_edit(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_edit.indexAt(button.parent().pos()).row()
            text = self.ui.tableWidget_edit.item(row, 0).text()
            sname_f(text)
            coo(5)
            UpdateDlg().exec_()
            self.init_edit()

    def find_edit(self):
        edit_index = self.ui.lineEdit_edit.text()
        if edit_index == "":
            self.ui.tableWidget_edit.setRowCount(0)
        else:
            sql = "select sname, type, address, settlement, credit " \
                  "from suppliers where sname like '%%%s%%'" % edit_index
            cursor = db.cursor()
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result = cursor.fetchall()
            if result is not None:
                row = cursor.rowcount
                self.ui.tableWidget_edit.setRowCount(row)
                result = list(result)
                for i in range(len(result)):
                    result[i] = list(result[i])
                for i in range(row):
                    self.ui.tableWidget_edit.setCellWidget(i, 5, self.button_edit())
                    for j in range(5):
                        if result[i][j] is not None:
                            item = QTableWidgetItem(str(result[i][j]))
                            item.setForeground(QBrush(QColor(255, 255, 255)))
                            self.ui.tableWidget_edit.setItem(i, j, item)
            cursor.close()

    def delete_edit(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_edit.indexAt(button.parent().pos()).row()
            text = self.ui.tableWidget_edit.item(row, 0).text()
            cursor = db.cursor()
            sql = "delete from suppliers where sname = '%s'" % text
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            db.commit()
            cursor.close()
            self.init_edit()

    def go_to_sup(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.init_sup()

    def go_to_anly(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.init_anly()

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

    def init_sup(self):
        cursor = db.cursor()
        sql = "select sname, gname from goods, suppliers " \
              "where suppliers.sno = goods.sno"
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        result = list(result)
        if result:
            row = cursor.rowcount
            self.ui.tableWidget_sup.setRowCount(row)
            for i in range(len(result)):
                result[i] = list(result[i])
            for i in range(row):
                self.ui.tableWidget_sup.setCellWidget(i, 2, self.button_sup())
                for j in range(2):
                    if result[i][j] is not None:
                        item = QTableWidgetItem(str(result[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_sup.setItem(i, j, item)
        else:
            self.ui.tableWidget_sup.setRowCount(0)
        cursor.close()

    def button_sup(self):
        widget = QtWidgets.QWidget()
        # 详情
        self.viewBtn = QtWidgets.QPushButton('详情')
        self.viewBtn.setStyleSheet(''' text-align : center;
                                                  background-color : Green;
                                                  height : 30px;
                                                  border-style: outset;
                                                  font : 13px  ''')
        self.viewBtn.clicked.connect(self.view_sup)

        # 修改
        self.updateBtn = QtWidgets.QPushButton('编辑')
        self.updateBtn.setStyleSheet(''' text-align : center;
                                          background-color : NavajoWhite;
                                          height : 30px;
                                          border-style: outset;
                                          font : 13px  ''')
        self.updateBtn.clicked.connect(self.update_sup)

        # 删除
        self.deleteBtn = QtWidgets.QPushButton('删除')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                    background-color : LightCoral;
                                    height : 30px;
                                    border-style: outset;
                                    font : 13px; ''')
        self.deleteBtn.clicked.connect(self.delete_sup)

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.viewBtn)
        hLayout.addWidget(self.updateBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def view_sup(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_sup.indexAt(button.parent().pos()).row()
            text1 = self.ui.tableWidget_sup.item(row, 0).text()
            text2 = self.ui.tableWidget_sup.item(row, 1).text()
            cursor = db.cursor()
            sql = "select * from goods where gname = '%s' and sno in " \
                  "(select sno from suppliers where sname = '%s')" % (text2, text1)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result = cursor.fetchall()
            if result is not None:
                result = list(result)
                for i in range(len(result)):
                    result[i] = list(result[i])
                sql = "select sname from suppliers where sno = '%s'" % result[0][3]
                try:
                    cursor.execute(sql)
                except Exception as r:
                    QMessageBox.critical(self, "错误", str(r))
                res = cursor.fetchall()
                res = list(res)
                for i in range(len(res)):
                    res[i] = list(res[i])
                mes = "货物：" + str(result[0][1]) + "\n单价：" + str(result[0][2]) + "\n供应商：" + str(res[0][0])
                QMessageBox.information(self, "消息", mes)
            cursor.close()

    def add_sup(self):
        coo(3)
        UpdateDlg().exec_()
        self.init_sup()

    def find_sup(self):
        sup_index = self.ui.lineEdit_sup.text()
        if sup_index == "":
            self.ui.tableWidget_sup.setRowCount(0)
        else:
            sql = "select sname, gname from goods, suppliers where suppliers.sno = goods.sno " \
                  "and suppliers.sname like '%%%s%%'" % sup_index
            cursor = db.cursor()
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result1 = cursor.fetchall()
            row1 = cursor.rowcount
            result1 = list(result1)
            if result1:
                for i in range(len(result1)):
                    result1[i] = list(result1[i])
            sql = "select sname, gname from goods, suppliers where suppliers.sno = goods.sno " \
                  "and goods.gname like '%%%s%%'" % sup_index
            cursor = db.cursor()
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result2 = cursor.fetchall()
            row2 = cursor.rowcount
            result2 = list(result2)
            if result2:
                for i in range(len(result2)):
                    result2[i] = list(result2[i])
            if row1 + row2 == 0:
                self.ui.tableWidget_sup.setRowCount(0)
            elif row1 > 0 and row2 == 0:
                self.ui.tableWidget_sup.setRowCount(row1)
                for i in range(row1):
                    self.ui.tableWidget_sup.setCellWidget(i, 2, self.button_sup())
                    for j in range(0, 2):
                        item = QTableWidgetItem(str(result1[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_sup.setItem(i, j, item)
            elif row1 == 0 and row2 > 0:
                self.ui.tableWidget_sup.setRowCount(row2)
                for i in range(row2):
                    self.ui.tableWidget_sup.setCellWidget(i, 2, self.button_sup())
                    for j in range(0, 2):
                        item = QTableWidgetItem(str(result2[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_sup.setItem(i, j, item)
            elif row1 > 0 and row2 > 0:
                result3 = []
                for i in result2:
                    if i not in result1:
                        result3.append(i)
                self.ui.tableWidget_sup.setRowCount(row1 + len(result3))
                for i in range(row1):
                    self.ui.tableWidget_sup.setCellWidget(i, 2, self.button_sup())
                    for j in range(2):
                        item = QTableWidgetItem(str(result1[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_sup.setItem(i, j, item)
                for i in range(len(result3)):
                    self.ui.tableWidget_sup.setCellWidget(i, 2, self.button_sup())
                    for j in range(2):
                        item = QTableWidgetItem(str(result3[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_sup.setItem(i + row1, j, item)
            cursor.close()

    def update_sup(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_sup.indexAt(button.parent().pos()).row()
            text1 = self.ui.tableWidget_sup.item(row, 0).text()
            text2 = self.ui.tableWidget_sup.item(row, 1).text()
            cursor = db.cursor()
            sql = "select gno from goods where gname = '%s' and sno in " \
                  "(select sno from suppliers where sname = '%s')" % (text2, text1)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result = cursor.fetchall()
            result = list(result)
            for i in range(len(result)):
                result[i] = list(result[i])
            gno_f(result[0][0])
            coo(0)
            UpdateDlg().exec_()
            self.init_sup()
            cursor.close()

    def delete_sup(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_sup.indexAt(button.parent().pos()).row()
            text1 = self.ui.tableWidget_sup.item(row, 0).text()
            text2 = self.ui.tableWidget_sup.item(row, 1).text()
            cursor = db.cursor()
            sql = "delete from goods where gname = '%s' and sno in " \
                  "(select sno from suppliers where sname = '%s')" % (text2, text1)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            db.commit()
            cursor.close()
            self.init_sup()

    def go_to_app(self):
        self.init_app()
        self.ui.stackedWidget.setCurrentIndex(1)

    def init_app(self):
        cursor = db.cursor()
        sql = "select sname, gname, quantity, pname, adate, astate " \
              "from suppliers, goods, applications " \
              "where goods.gno = applications.gno and suppliers.sno = goods.sno"
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        result = list(result)
        if result:
            row = cursor.rowcount
            self.ui.tableWidget_app.setRowCount(row)
            for i in range(len(result)):
                result[i] = list(result[i])
            for i in range(row):
                if result[i][5] == "审核中":
                    self.ui.tableWidget_app.setCellWidget(i, 6, self.button_app())
                else:
                    self.ui.tableWidget_app.setCellWidget(i, 6, self.button_app1())
                for j in range(6):
                    if result[i][j] is not None:
                        item = QTableWidgetItem(str(result[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_app.setItem(i, j, item)
        else:
            self.ui.tableWidget_app.setRowCount(0)
        cursor.close()

    def button_app(self):
        widget = QtWidgets.QWidget()

        self.passBtn = QtWidgets.QPushButton('通过')
        self.passBtn.setStyleSheet(''' text-align : center;
                                                          background-color : Green;
                                                          height : 30px;
                                                          border-style: outset;
                                                          font : 13px  ''')
        self.passBtn.clicked.connect(self.pass_)

        self.unpassBtn = QtWidgets.QPushButton('拒绝')
        self.unpassBtn.setStyleSheet(''' text-align : center;
                                                  background-color : NavajoWhite;
                                                  height : 30px;
                                                  border-style: outset;
                                                  font : 13px  ''')
        self.unpassBtn.clicked.connect(self.unpass)

        # 删除
        self.deleteBtn = QtWidgets.QPushButton('删除')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                            background-color : LightCoral;
                                            height : 30px;
                                            border-style: outset;
                                            font : 13px; ''')
        self.deleteBtn.clicked.connect(self.delete_app)

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.passBtn)
        hLayout.addWidget(self.unpassBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def button_app1(self):
        widget = QtWidgets.QWidget()
        self.deleteBtn = QtWidgets.QPushButton('删除')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                            background-color : LightCoral;
                                            height : 30px;
                                            border-style: outset;
                                            font : 13px; ''')
        self.deleteBtn.clicked.connect(self.delete_app)

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def pass_(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_app.indexAt(button.parent().pos()).row()
            text1 = self.ui.tableWidget_app.item(row, 0).text()
            text2 = self.ui.tableWidget_app.item(row, 1).text()
            cursor = db.cursor()
            sql = "select ano from applications where gno in " \
                  "(select gno from goods where gname = '%s') " \
                  "and gno in (select gno from goods where sno in " \
                  "(select sno from suppliers where sname = '%s'))" % (text2, text1)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result = cursor.fetchall()
            result = list(result)
            if result:
                for i in range(len(result)):
                    result[i] = list(result[i])
                ano_f(result[0][0])
                coo(7)
                UpdateDlg().exec_()
            cursor.close()
            self.init_app()

    def unpass(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_sup.indexAt(button.parent().pos()).row()
            text1 = self.ui.tableWidget_app.item(row, 0).text()
            text2 = self.ui.tableWidget_app.item(row, 1).text()
            cursor = db.cursor()
            sql = "update applications set astate = '已拒绝' where gno in " \
                  "(select gno from goods where gname = '%s') " \
                  "and gno in (select gno from goods where sno in " \
                  "(select sno from suppliers where sname = '%s'))" % (text2, text1)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            db.commit()
            cursor.close()
            self.init_app()

    def delete_app(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_sup.indexAt(button.parent().pos()).row()
            text1 = self.ui.tableWidget_app.item(row, 0).text()
            text2 = self.ui.tableWidget_app.item(row, 1).text()
            cursor = db.cursor()
            sql = "delete from applications where gno in " \
                  "(select gno from goods where gname = '%s') " \
                  "and gno in (select gno from goods where sno in " \
                  "(select sno from suppliers where sname = '%s'))" % (text2, text1)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            db.commit()
            cursor.close()
        self.init_app()

    def add_app(self):
        coo(1)
        UpdateDlg().exec_()
        self.init_app()

    def find_app(self):
        app_index = self.ui.lineEdit_app.text()
        if app_index == "":
            self.ui.tableWidget_app.setRowCount(0)
        else:
            sql = "select sname, gname, quantity, pname, adate, astate " \
                  "from goods, suppliers, applications " \
                  "where goods.gno = applications.gno and suppliers.sno = goods.sno " \
                  "and suppliers.sname like '%%%s%%'" % app_index
            cursor = db.cursor()
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result1 = cursor.fetchall()
            row1 = cursor.rowcount
            result1 = list(result1)
            if result1:
                for i in range(len(result1)):
                    result1[i] = list(result1[i])
            sql = "select sname, gname, quantity, pname, adate, astate " \
                  "from goods, suppliers, applications " \
                  "where goods.gno = applications.gno and suppliers.sno = goods.sno " \
                  "and goods.gname like '%%%s%%'" % app_index
            cursor = db.cursor()
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result2 = cursor.fetchall()
            row2 = cursor.rowcount
            result2 = list(result2)
            if result2:
                for i in range(len(result2)):
                    result2[i] = list(result2[i])
            if row1 + row2 == 0:
                self.ui.tableWidget_app.setRowCount(0)
            elif row1 > 0 and row2 == 0:
                self.ui.tableWidget_app.setRowCount(row1)
                for i in range(row1):
                    if result1[i][5] == "审核中":
                        self.ui.tableWidget_app.setCellWidget(i, 6, self.button_app())
                    else:
                        self.ui.tableWidget_app.setCellWidget(i, 6, self.button_app1())
                    for j in range(0, 2):
                        item = QTableWidgetItem(str(result1[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_app.setItem(i, j, item)
            elif row1 == 0 and row2 > 0:
                self.ui.tableWidget_app.setRowCount(row2)
                for i in range(row2):
                    if result2[i][5] == "审核中":
                        self.ui.tableWidget_app.setCellWidget(i, 6, self.button_app())
                    else:
                        self.ui.tableWidget_app.setCellWidget(i, 6, self.button_app1())
                    for j in range(0, 2):
                        item = QTableWidgetItem(str(result2[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_app.setItem(i, j, item)
            elif row1 > 0 and row2 > 0:
                result3 = []
                for i in result2:
                    if i not in result1:
                        result3.append(i)
                self.ui.tableWidget_app.setRowCount(row1 + len(result3))
                for i in range(row1):
                    if result1[i][5] == "审核中":
                        self.ui.tableWidget_app.setCellWidget(i, 6, self.button_app())
                    else:
                        self.ui.tableWidget_app.setCellWidget(i, 6, self.button_app1())
                    for j in range(0, 2):
                        item = QTableWidgetItem(str(result1[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_app.setItem(i, j, item)
                for i in range(len(result3)):
                    if result3[i][5] == "审核中":
                        self.ui.tableWidget_app.setCellWidget(i, 6, self.button_app())
                    else:
                        self.ui.tableWidget_app.setCellWidget(i, 6, self.button_app1())
                    for j in range(2):
                        item = QTableWidgetItem(str(result3[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_app.setItem(i + row1, j, item)
            cursor.close()

    def go_to_buy(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self.init_buy()

    def init_buy(self):
        cursor = db.cursor()
        sql = "select sname, gname, bname, bdate, bstate " \
              "from suppliers, goods, buying where bno in " \
              "(select bno from documents where ano in " \
              "(select ano from applications where goods.gno = applications.gno " \
              "and suppliers.sno = goods.sno))"
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        result = list(result)
        if result:
            row = cursor.rowcount
            self.ui.tableWidget_buy.setRowCount(row)
            for i in range(len(result)):
                result[i] = list(result[i])
            for i in range(row):
                if result[i][4] == "验货":
                    self.ui.tableWidget_buy.setCellWidget(i, 5, self.button_buy())
                else:
                    self.ui.tableWidget_buy.setCellWidget(i, 5, self.button_buy1())
                for j in range(5):
                    if result[i][j] is not None:
                        item = QTableWidgetItem(str(result[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_buy.setItem(i, j, item)
        else:
            self.ui.tableWidget_buy.setRowCount(0)
        cursor.close()

    def button_buy(self):
        widget = QtWidgets.QWidget()

        self.passBtn = QtWidgets.QPushButton('收货')
        self.passBtn.setStyleSheet(''' text-align : center;
                                                  background-color : Green;
                                                  height : 30px;
                                                  border-style: outset;
                                                  font : 13px  ''')
        self.passBtn.clicked.connect(self.pass_buy)

        self.unpassBtn = QtWidgets.QPushButton('退货')
        self.unpassBtn.setStyleSheet(''' text-align : center;
                                                    background-color : NavajoWhite;
                                                    height : 30px;
                                                    border-style: outset;
                                                    font : 13px; ''')
        self.unpassBtn.clicked.connect(self.unpass_buy)

        widget = QtWidgets.QWidget()
        self.deleteBtn = QtWidgets.QPushButton('删除')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                                    background-color : LightCoral;
                                                    height : 30px;
                                                    border-style: outset;
                                                    font : 13px; ''')
        self.deleteBtn.clicked.connect(self.delete_buy)

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.passBtn)
        hLayout.addWidget(self.unpassBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def button_buy1(self):
        widget = QtWidgets.QWidget()
        self.deleteBtn = QtWidgets.QPushButton('删除')
        self.deleteBtn.setStyleSheet(''' text-align : center;
                                            background-color : LightCoral;
                                            height : 30px;
                                            border-style: outset;
                                            font : 13px; ''')
        self.deleteBtn.clicked.connect(self.delete_buy)

        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def pass_buy(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_buy.indexAt(button.parent().pos()).row()
            text1 = self.ui.tableWidget_buy.item(row, 0).text()
            text2 = self.ui.tableWidget_buy.item(row, 1).text()
            cursor = db.cursor()
            sql = "update buying set bstate = '收货' " \
                  "where bno in (select bno from documents " \
                  "where ano in (select ano from applications " \
                  "where gno in (select gno from goods where gname = '%s') " \
                  "and gno in (select gno from goods where sno in (" \
                  "select sno from suppliers where sname = '%s'))))" % (text2, text1)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            db.commit()
            cursor.close()
            self.init_buy()

    def unpass_buy(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_buy.indexAt(button.parent().pos()).row()
            text1 = self.ui.tableWidget_buy.item(row, 0).text()
            text2 = self.ui.tableWidget_buy.item(row, 1).text()
            cursor = db.cursor()
            sql = "update buying set bstate = '退货' " \
                  "where bno in (select bno from documents " \
                  "where ano in (select ano from applications " \
                  "where gno in (select gno from goods where gname = '%s') " \
                  "and gno in (select gno from goods where sno in (" \
                  "select sno from suppliers where sname = '%s'))))" % (text2, text1)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            db.commit()
            cursor.close()
            self.init_buy()

    def delete_buy(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_buy.indexAt(button.parent().pos()).row()
            text1 = self.ui.tableWidget_buy.item(row, 0).text()
            text2 = self.ui.tableWidget_buy.item(row, 1).text()
            cursor = db.cursor()
            sql = "SET foreign_key_checks = 0"
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            sql = "delete from buying " \
                  "where bno in (select bno from documents " \
                  "where ano in (select ano from applications " \
                  "where gno in (select gno from goods where gname = '%s') " \
                  "and gno in (select gno from goods where sno in (" \
                  "select sno from suppliers where sname = '%s'))))" % (text2, text1)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            sql = "delete from applications where gno in " \
                  "(select gno from goods where gname = '%s') " \
                  "and gno in (select gno from goods where sno in " \
                  "(select sno from suppliers where sname = '%s'))" % (text2, text1)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            sql = "SET foreign_key_checks = 1"
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            db.commit()
            cursor.close()
        self.init_buy()

    def find_buy(self):
        buy_index = self.ui.lineEdit_buy.text()
        if buy_index == "":
            self.ui.tableWidget_buy.setRowCount(0)
        else:
            sql = "select sname, gname, bname, bdate, bstate " \
              "from suppliers, goods, buying where bno in " \
              "(select bno from documents where ano in " \
              "(select ano from applications where goods.gno = applications.gno " \
              "and suppliers.sno = goods.sno)) and sname like '%%%s%%'" % buy_index
            cursor = db.cursor()
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result1 = cursor.fetchall()
            row1 = cursor.rowcount
            result1 = list(result1)
            if result1:
                for i in range(len(result1)):
                    result1[i] = list(result1[i])
            sql = "select sname, gname, bname, bdate, bstate " \
                  "from suppliers, goods, buying where bno in " \
                  "(select bno from documents where ano in " \
                  "(select ano from applications where goods.gno = applications.gno " \
                  "and suppliers.sno = goods.sno)) and gname like '%%%s%%'" % buy_index
            cursor = db.cursor()
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result2 = cursor.fetchall()
            row2 = cursor.rowcount
            result2 = list(result2)
            if result2:
                for i in range(len(result2)):
                    result2[i] = list(result2[i])
            if row1 + row2 == 0:
                self.ui.tableWidget_buy.setRowCount(0)
            elif row1 > 0 and row2 == 0:
                self.ui.tableWidget_buy.setRowCount(row1)
                for i in range(row1):
                    if result1[i][4] == "验货":
                        self.ui.tableWidget_buy.setCellWidget(i, 5, self.button_buy())
                    else:
                        self.ui.tableWidget_buy.setCellWidget(i, 5, self.button_buy1())
                    for j in range(0, 2):
                        item = QTableWidgetItem(str(result1[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_buy.setItem(i, j, item)
            elif row1 == 0 and row2 > 0:
                self.ui.tableWidget_buy.setRowCount(row2)
                for i in range(row2):
                    if result2[i][4] == "验货":
                        self.ui.tableWidget_buy.setCellWidget(i, 5, self.button_buy())
                    else:
                        self.ui.tableWidget_buy.setCellWidget(i, 5, self.button_buy1())
                    for j in range(0, 2):
                        item = QTableWidgetItem(str(result2[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_buy.setItem(i, j, item)
            elif row1 > 0 and row2 > 0:
                result3 = []
                for i in result2:
                    if i not in result1:
                        result3.append(i)
                self.ui.tableWidget_buy.setRowCount(row1 + len(result3))
                for i in range(row1):
                    if result1[i][4] == "验货":
                        self.ui.tableWidget_buy.setCellWidget(i, 5, self.button_buy())
                    else:
                        self.ui.tableWidget_buy.setCellWidget(i, 5, self.button_buy1())
                    for j in range(0, 2):
                        item = QTableWidgetItem(str(result1[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_buy.setItem(i, j, item)
                for i in range(len(result3)):
                    if result3[i][4] == "验货":
                        self.ui.tableWidget_buy.setCellWidget(i + row1, 5, self.button_buy())
                    else:
                        self.ui.tableWidget_buy.setCellWidget(i + row1, 5, self.button_buy1())
                    for j in range(2):
                        item = QTableWidgetItem(str(result3[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_buy.setItem(i + row1, j, item)
            cursor.close()

    def go_to_doc(self):
        self.init_doc()

    def init_doc(self):
        cursor = db.cursor()
        sql = "select sname, gname, quantity, pname, bname " \
              "from suppliers, goods, applications, buying,documents " \
              "where documents.ano in (select ano from applications " \
              "where goods.gno = applications.gno and suppliers.sno = goods.sno) " \
              "and documents.bno = buying.bno and documents.ano = applications.ano"
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        result = list(result)
        if result:
            row = cursor.rowcount
            self.ui.tableWidget_anly.setRowCount(row)
            for i in range(len(result)):
                result[i] = list(result[i])
            for i in range(row):
                for j in range(5):
                    if result[i][j] is not None:
                        item = QTableWidgetItem(str(result[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_anly.setItem(i, j, item)
        else:
            self.ui.tableWidget_anly.setRowCount(0)
        cursor.close()

    def find_doc(self):
        doc_index = self.ui.lineEdit_anly.text()
        if doc_index == "":
            self.ui.tableWidget_anly.setRowCount(0)
        else:
            sql = "select sname, gname, quantity, pname, bname " \
              "from suppliers, goods, applications, buying,documents " \
              "where documents.ano in (select ano from applications " \
              "where goods.gno = applications.gno and suppliers.sno = goods.sno) " \
              "and documents.bno = buying.bno and documents.ano = applications.ano " \
                  "and sname like '%%%s%%'" % doc_index
            cursor = db.cursor()
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result1 = cursor.fetchall()
            row1 = cursor.rowcount
            result1 = list(result1)
            if result1:
                for i in range(len(result1)):
                    result1[i] = list(result1[i])
            sql = "select sname, gname, quantity, pname, bname " \
                  "from suppliers, goods, applications, buying,documents " \
                  "where documents.ano in (select ano from applications " \
                  "where goods.gno = applications.gno and suppliers.sno = goods.sno) " \
                  "and documents.bno = buying.bno and documents.ano = applications.ano " \
                  "and gname like '%%%s%%'" % doc_index
            cursor = db.cursor()
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result2 = cursor.fetchall()
            row2 = cursor.rowcount
            result2 = list(result2)
            if result2:
                for i in range(len(result2)):
                    result2[i] = list(result2[i])
            if row1 + row2 == 0:
                self.ui.tableWidget_anly.setRowCount(0)
            elif row1 > 0 and row2 == 0:
                self.ui.tableWidget_anly.setRowCount(row1)
                for i in range(row1):
                    for j in range(5):
                        item = QTableWidgetItem(str(result1[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_anly.setItem(i, j, item)
            elif row1 == 0 and row2 > 0:
                self.ui.tableWidget_anly.setRowCount(row2)
                for i in range(row2):
                    for j in range(5):
                        item = QTableWidgetItem(str(result2[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_anly.setItem(i, j, item)
            elif row1 > 0 and row2 > 0:
                result3 = []
                for i in result2:
                    if i not in result1:
                        result3.append(i)
                self.ui.tableWidget_anly.setRowCount(row1 + len(result3))
                for i in range(row1):
                    for j in range(5):
                        item = QTableWidgetItem(str(result1[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_anly.setItem(i, j, item)
                for i in range(len(result3)):
                    for j in range(2):
                        item = QTableWidgetItem(str(result3[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_anly.setItem(i + row1, j, item)
            cursor.close()

    def init_anly(self):
        cursor = db.cursor()
        sql = "select * from analyse"
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        if result is not None:
            row = cursor.rowcount
            self.ui.tableWidget_doc.setRowCount(row)
            result = list(result)
            for i in range(len(result)):
                result[i] = list(result[i])
            for i in range(row):
                self.ui.tableWidget_doc.setCellWidget(i, 2, self.button_anly())
                for j in range(2):
                    if result[i][j] is not None:
                        item = QTableWidgetItem(str(result[i][j]))
                        item.setForeground(QBrush(QColor(255, 255, 255)))
                        self.ui.tableWidget_doc.setItem(i, j, item)
        cursor.close()

    def button_anly(self):
        widget = QtWidgets.QWidget()
        # 详情
        self.viewBtn = QtWidgets.QPushButton('详情')
        self.viewBtn.setStyleSheet(''' text-align : center;
                                                          background-color : Green;
                                                          height : 30px;
                                                          border-style: outset;
                                                          font : 13px  ''')
        self.viewBtn.clicked.connect(self.view_anly)
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.viewBtn)
        hLayout.setContentsMargins(5, 2, 5, 2)
        widget.setLayout(hLayout)
        return widget

    def view_anly(self):
        button = self.sender()
        if button:
            row = self.ui.tableWidget_doc.indexAt(button.parent().pos()).row()
            gname_f(self.ui.tableWidget_doc.item(row, 0).text())
        coo(6)
        UpdateDlg().exec_()

    def find_anly(self):
        anly_index = self.ui.lineEdit_doc.text()
        if anly_index == "":
            self.ui.tableWidget_doc.setRowCount(0)
        else:
            sql = "select * from analyse where gname like '%%%s%%'" % anly_index
            cursor = db.cursor()
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result = cursor.fetchall()
            if result is not None:
                row = cursor.rowcount
                self.ui.tableWidget_doc.setRowCount(row)
                result = list(result)
                for i in range(len(result)):
                    result[i] = list(result[i])
                for i in range(row):
                    self.ui.tableWidget_doc.setCellWidget(i, 2, self.button_anly())
                    for j in range(2):
                        if result[i][j] is not None:
                            item = QTableWidgetItem(str(result[i][j]))
                            item.setForeground(QBrush(QColor(255, 255, 255)))
                            self.ui.tableWidget_doc.setItem(i, j, item)
            cursor.close()

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


class UpdateDlg(QtWidgets.QDialog):
    def __init__(self):
        super(UpdateDlg, self).__init__()
        self.ui = Ui_UpdateDlg()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentIndex(a)
        self.init_anly()
        self.ui.pushButton_edit.clicked.connect(self.add_edit)
        self.ui.pushButton_edit2.clicked.connect(self.update_edit)
        self.ui.pushButton_supYes.clicked.connect(self.update_sup)
        self.ui.pushButton_supYes2.clicked.connect(self.add_sup)
        self.ui.pushButton_pname.clicked.connect(self.add_pname)
        self.ui.pushButton_app.clicked.connect(self.add_app)

    def add_edit(self):
        cursor = db.cursor()
        sname = self.ui.lineEdit_sn.text()
        type = self.ui.comboBox_type.currentText()
        addr = self.ui.lineEdit_addr.text()
        stl = self.ui.comboBox_stl.currentText()
        crd = self.ui.comboBox_crd.currentText()
        sql = "select * from suppliers"
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        no = 0
        sname_index = True
        result = list(result)
        if result:
            row = cursor.rowcount
            for i in range(len(result)):
                result[i] = list(result[i])
            for i in range(row):
                no = result[i][0]
                if result[i][1] == sname:
                    QMessageBox.critical(self, "错误", "已存在该供应商")
                    sname_index = False
                    break
        if sname_index:
            no = int(no) + 1
            if no < 10:
                str_no = "0" + str(no)
            else:
                str_no = str(no)
            sql = "insert into suppliers values ('%s', '%s', '%s', '%s', '%s', '%s')" % (str_no, sname, type, addr, stl, crd)
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            db.commit()
            QMessageBox.information(self, "消息", "添加成功")
            self.close()
        cursor.close()

    def update_edit(self):
        cursor = db.cursor()
        sname = self.ui.lineEdit_sn2.text()
        type = self.ui.comboBox_type2.currentText()
        addr = self.ui.lineEdit_addr2.text()
        stl = self.ui.comboBox_stl2.currentText()
        crd = self.ui.comboBox_crd2.currentText()
        sql = "select * from suppliers"
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        no = 0
        sname_index = True
        result = list(result)
        if result:
            row = cursor.rowcount
            for i in range(len(result)):
                result[i] = list(result[i])
            for i in range(row):
                no = result[i][0]
                if result[i][1] == sname:
                    QMessageBox.critical(self, "错误", "已存在该供应商")
                    sname_index = False
                    break
        if sname_index:
            sql1 = "update suppliers set sname = '%s' where sname = '%s'" % (sname, sname_i)
            sql2 = "update suppliers set type = '%s' where sname = '%s'" % (type, sname_i)
            sql3 = "update suppliers set address = '%s' where sname = '%s'" % (addr, sname_i)
            sql4 = "update suppliers set settlement = '%s' where sname = '%s'" % (stl, sname_i)
            sql5 = "update suppliers set credit = '%s' where sname = '%s'" % (crd, sname_i)
            try:
                cursor.execute(sql1)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            try:
                cursor.execute(sql2)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            try:
                cursor.execute(sql3)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            try:
                cursor.execute(sql4)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            try:
                cursor.execute(sql5)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            db.commit()
            QMessageBox.information(self, "消息", "修改成功")
            self.close()
        cursor.close()

    def add_sup(self):
        cursor = db.cursor()
        gname = self.ui.lineEdit_gname2.text()
        price = self.ui.lineEdit_price2.text()
        sname = self.ui.lineEdit_sname2.text()
        sql = "select sno from suppliers where sname = '%s'" % sname
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        result = list(result)
        if not result:
            QMessageBox.critical(self, "错误", "不存在该供应商")
        else:
            for i in range(len(result)):
                result[i] = list(result[i])
            sno = result[0][0]
            sql = "select gname from goods where sno = '%s'" % sno
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result = cursor.fetchall()
            result = list(result)
            exist_index = True
            if result:
                for i in range(len(result)):
                    result[i] = list(result[i])
                if result[0][0] == gname:
                    QMessageBox.critical(self, "错误", "已存在该货物")
                    exist_index = False
            if exist_index:
                sql = "select * from goods"
                try:
                    cursor.execute(sql)
                except Exception as r:
                    QMessageBox.critical(self, "错误", str(r))
                row = cursor.rowcount
                result = cursor.fetchall()
                no = 0
                result = list(result)
                if result:
                    for i in range(len(result)):
                        result[i] = list(result[i])
                    for i in range(row):
                        no = result[i][0]
                no = int(no) + 1
                if no < 10:
                    str_no = "0" + str(no)
                else:
                    str_no = str(no)
                sql = "insert into goods values ('%s', '%s', %s, '%s')" % (str_no, gname, price, sno)
                try:
                    cursor.execute(sql)
                except Exception as r:
                    QMessageBox.critical(self, "错误", str(r))
                db.commit()
                QMessageBox.information(self, "消息", "添加成功")
                self.close()
        cursor.close()

    def update_sup(self):
        cursor = db.cursor()
        gname = self.ui.lineEdit_gname.text()
        price = self.ui.lineEdit_price.text()
        sname = self.ui.lineEdit_sname.text()
        sql = "select sno from suppliers where sname = '%s'" % sname
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        if result is None:
            QMessageBox.critical(self, "错误", "不存在该供应商")
        else:
            result = list(result)
            if not result:
                QMessageBox.critical(self, "错误", "不存在该供应商")
            else:
                for i in range(len(result)):
                    result[i] = list(result[i])
                sno = result[0][0]
                sql1 = "update goods set gname = '%s' where gno = '%s'" % (gname, gno_g)
                sql2 = "update goods set price = %s where gno = %s" % (price, gno_g)
                sql3 = "update goods set sno = '%s' where gno = '%s'" % (sno, gno_g)
                try:
                    cursor.execute(sql1)
                except Exception as r:
                    QMessageBox.critical(self, "错误", str(r))
                try:
                    cursor.execute(sql2)
                except Exception as r:
                    QMessageBox.critical(self, "错误", str(r))
                try:
                    cursor.execute(sql3)
                except Exception as r:
                    QMessageBox.critical(self, "错误", str(r))
                db.commit()
                QMessageBox.information(self, "消息", "修改成功")
                self.close()
            cursor.close()

    def add_app(self):
        sname = self.ui.lineEdit_aSup.text()
        gname = self.ui.lineEdit_aGoods.text()
        quan = self.ui.lineEdit_aQuan.text()
        pname = self.ui.lineEdit_aP.text()
        cursor = db.cursor()
        sql = "select sno from suppliers where sname = '%s'" % sname
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        result = list(result)
        if not result:
            QMessageBox.critical(self, "错误", "不存在该供应商")
        else:
            for i in range(len(result)):
                result[i] = list(result[i])
            sno = result[0][0]
            sql = "select gname, gno from goods where sno = '%s'" % sno
            try:
                cursor.execute(sql)
            except Exception as r:
                QMessageBox.critical(self, "错误", str(r))
            result = cursor.fetchall()
            row = cursor.rowcount
            result = list(result)
            exist_index = False
            exist_index2 = False
            if result:
                for i in range(len(result)):
                    result[i] = list(result[i])
                for i in range(row):
                    if result[i][0] == gname:
                        exist_index = True
                        gn = result[i][1]
                        exist_index2 = True
            if not exist_index2:
                QMessageBox.critical(self, "错误", "该供应商不提供该货物")
            if exist_index:
                sql = "select * from applications"
                try:
                    cursor.execute(sql)
                except Exception as r:
                    QMessageBox.critical(self, "错误", str(r))
                row = cursor.rowcount
                result = cursor.fetchall()
                no = 0
                result = list(result)
                if result:
                    for i in range(len(result)):
                        result[i] = list(result[i])
                    for i in range(row):
                        no = result[i][0]
                no = int(no) + 1
                if no < 10:
                    str_no = "0" + str(no)
                else:
                    str_no = str(no)
                sql = "insert into applications values ('%s', '%s', %s, '%s', default, default)" % (str_no, gn, quan, pname)
                try:
                    cursor.execute(sql)
                except Exception as r:
                    QMessageBox.critical(self, "错误", str(r))
                db.commit()
                QMessageBox.information(self, "消息", "添加成功")
                self.close()
        cursor.close()

    def init_anly(self):
        if gname is not None:
            self.ui.label_goods.setText(gname)
        sql = "call anly()"
        cursor = db.cursor()
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        sql = "select sname, type, credit from suppliers " \
              "where sno in (select sno from goods where gname = '%s')" % gname
        cursor = db.cursor()
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        if result is not None:
            row = cursor.rowcount
            self.ui.tableWidget_anly.setRowCount(row)
            result = list(result)
            for i in range(len(result)):
                result[i] = list(result[i])
            for i in range(row):
                for j in range(3):
                    if result[i][j] is not None:
                        item = QTableWidgetItem(str(result[i][j]))
                        item.setForeground(QBrush(QColor(0, 0, 0)))
                        self.ui.tableWidget_anly.setItem(i, j, item)
        cursor.close()

    def add_pname(self):
        pname = self.ui.lineEdit_pname.text()
        cursor = db.cursor()

        sql = "select bno from buying"
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        result = list(result)
        if not result:
            no = "0"
        else:
            result[0] = list(result[0])
            for i in range(len(result)):
                no = result[i][0]
        str_no = str(int(no) + 1)
        if int(str_no) < 10:
            str_no = "0" + str_no
        sql = "insert into buying values ('%s', default, '%s', default)" % (str_no, pname)
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))

        sql = "select dno from documents"
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        result = cursor.fetchall()
        result = list(result)
        if not result:
            no = "0"
        else:
            result[0] = list(result[0])
            for i in range(len(result)):
                no = result[i][0]
        str_no2 = str(int(no) + 1)
        if int(str_no2) < 10:
            str_no2 = "0" + str_no2
        sql = "insert into documents values ('%s', '%s', '%s')" % (str_no2, ano, str_no)
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))

        sql = "update applications set astate = '已通过' where ano = '%s'" % ano
        try:
            cursor.execute(sql)
        except Exception as r:
            QMessageBox.critical(self, "错误", str(r))
        db.commit()
        cursor.close()
        self.close()

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
