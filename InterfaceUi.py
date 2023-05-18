# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InterfaceUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1105, 715)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame{\n"
"    background-color: rgb(56, 57, 60);\n"
"    border-radius:30px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("#frame_2{\n"
"    background-color: rgb(86, 88, 93);\n"
"    border-top-left-radius:30px;\n"
"    border-top-right-radius:30px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(200, 0))
        self.frame_4.setStyleSheet("QPushButton{\n"
"    border:none;\n"
"}\n"
"QPushButton:hover{\n"
"    padding-bottom:5px;\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_maxsize = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_maxsize.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/maxmize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_maxsize.setIcon(icon)
        self.pushButton_maxsize.setObjectName("pushButton_maxsize")
        self.horizontalLayout_2.addWidget(self.pushButton_maxsize)
        self.pushButton_minisize = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_minisize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/minus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_minisize.setIcon(icon1)
        self.pushButton_minisize.setObjectName("pushButton_minisize")
        self.horizontalLayout_2.addWidget(self.pushButton_minisize)
        self.pushButton_close = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_close.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_close.setIcon(icon2)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_2.addWidget(self.pushButton_close)
        self.horizontalLayout_3.addWidget(self.frame_4, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(102, 133, 156, 255), stop:1 rgba(117, 255, 201, 255));\n"
"    border:none;\n"
"    border-radius:7px;\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"}\n"
"#frame_5{\n"
"    background-color: rgb(77, 79, 83);\n"
"    border-bottom-left-radius:30px;\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_sup = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_sup.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_sup.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_sup.setObjectName("pushButton_sup")
        self.verticalLayout_3.addWidget(self.pushButton_sup)
        self.pushButton_app = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_app.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_app.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_app.setObjectName("pushButton_app")
        self.verticalLayout_3.addWidget(self.pushButton_app)
        self.pushButton_buy = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_buy.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_buy.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_buy.setObjectName("pushButton_buy")
        self.verticalLayout_3.addWidget(self.pushButton_buy)
        self.pushButton_doc = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_doc.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_doc.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_doc.setObjectName("pushButton_doc")
        self.verticalLayout_3.addWidget(self.pushButton_doc)
        self.pushButton_anly = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_anly.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_anly.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_anly.setObjectName("pushButton_anly")
        self.verticalLayout_3.addWidget(self.pushButton_anly)
        self.pushButton_exit = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_exit.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_exit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.verticalLayout_3.addWidget(self.pushButton_exit)
        self.horizontalLayout_4.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_6)
        self.stackedWidget.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_sup = QtWidgets.QWidget()
        self.page_sup.setObjectName("page_sup")
        self.tableWidget_sup = QtWidgets.QTableWidget(self.page_sup)
        self.tableWidget_sup.setGeometry(QtCore.QRect(0, 40, 901, 541))
        self.tableWidget_sup.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.tableWidget_sup.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_sup.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_sup.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_sup.setObjectName("tableWidget_sup")
        self.tableWidget_sup.setColumnCount(4)
        self.tableWidget_sup.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sup.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sup.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sup.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_sup.setHorizontalHeaderItem(3, item)
        self.tableWidget_sup.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_sup.verticalHeader().setVisible(False)
        self.pushButton_supAdd = QtWidgets.QPushButton(self.page_sup)
        self.pushButton_supAdd.setGeometry(QtCore.QRect(20, 0, 93, 28))
        self.pushButton_supAdd.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    font: 12pt \"楷体\";\n"
"    border:none;\n"
"    border-radius:7px;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_supAdd.setObjectName("pushButton_supAdd")
        self.pushButton_supFind = QtWidgets.QPushButton(self.page_sup)
        self.pushButton_supFind.setGeometry(QtCore.QRect(130, 0, 93, 28))
        self.pushButton_supFind.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    font: 12pt \"楷体\";\n"
"    border:none;\n"
"    border-radius:7px;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_supFind.setObjectName("pushButton_supFind")
        self.stackedWidget.addWidget(self.page_sup)
        self.page_app = QtWidgets.QWidget()
        self.page_app.setObjectName("page_app")
        self.pushButton_appAdd = QtWidgets.QPushButton(self.page_app)
        self.pushButton_appAdd.setGeometry(QtCore.QRect(20, 0, 93, 28))
        self.pushButton_appAdd.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 170, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    font: 12pt \"楷体\";\n"
"    border:none;\n"
"    border-radius:7px;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_appAdd.setObjectName("pushButton_appAdd")
        self.tableWidget_app = QtWidgets.QTableWidget(self.page_app)
        self.tableWidget_app.setGeometry(QtCore.QRect(0, 40, 901, 541))
        self.tableWidget_app.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.tableWidget_app.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_app.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_app.setObjectName("tableWidget_app")
        self.tableWidget_app.setColumnCount(7)
        self.tableWidget_app.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_app.setHorizontalHeaderItem(6, item)
        self.tableWidget_app.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_app.verticalHeader().setVisible(False)
        self.pushButton_appFind = QtWidgets.QPushButton(self.page_app)
        self.pushButton_appFind.setGeometry(QtCore.QRect(130, 0, 93, 28))
        self.pushButton_appFind.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    font: 12pt \"楷体\";\n"
"    border:none;\n"
"    border-radius:7px;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_appFind.setObjectName("pushButton_appFind")
        self.stackedWidget.addWidget(self.page_app)
        self.page_buy = QtWidgets.QWidget()
        self.page_buy.setObjectName("page_buy")
        self.tableWidget_buy = QtWidgets.QTableWidget(self.page_buy)
        self.tableWidget_buy.setGeometry(QtCore.QRect(0, 40, 901, 541))
        self.tableWidget_buy.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.tableWidget_buy.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_buy.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_buy.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_buy.setObjectName("tableWidget_buy")
        self.tableWidget_buy.setColumnCount(6)
        self.tableWidget_buy.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_buy.setHorizontalHeaderItem(5, item)
        self.tableWidget_buy.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_buy.verticalHeader().setVisible(False)
        self.pushButton_appFind_2 = QtWidgets.QPushButton(self.page_buy)
        self.pushButton_appFind_2.setGeometry(QtCore.QRect(30, 0, 93, 28))
        self.pushButton_appFind_2.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    font: 12pt \"楷体\";\n"
"    border:none;\n"
"    border-radius:7px;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_appFind_2.setObjectName("pushButton_appFind_2")
        self.stackedWidget.addWidget(self.page_buy)
        self.page_anly = QtWidgets.QWidget()
        self.page_anly.setObjectName("page_anly")
        self.tableWidget_anly = QtWidgets.QTableWidget(self.page_anly)
        self.tableWidget_anly.setGeometry(QtCore.QRect(0, 40, 901, 541))
        self.tableWidget_anly.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.tableWidget_anly.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_anly.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_anly.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_anly.setObjectName("tableWidget_anly")
        self.tableWidget_anly.setColumnCount(6)
        self.tableWidget_anly.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anly.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anly.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anly.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anly.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anly.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_anly.setHorizontalHeaderItem(5, item)
        self.tableWidget_anly.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_anly.verticalHeader().setVisible(False)
        self.pushButton_anlyFind = QtWidgets.QPushButton(self.page_anly)
        self.pushButton_anlyFind.setGeometry(QtCore.QRect(30, 0, 93, 28))
        self.pushButton_anlyFind.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    font: 12pt \"楷体\";\n"
"    border:none;\n"
"    border-radius:7px;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_anlyFind.setObjectName("pushButton_anlyFind")
        self.stackedWidget.addWidget(self.page_anly)
        self.page_doc = QtWidgets.QWidget()
        self.page_doc.setObjectName("page_doc")
        self.tableWidget_doc = QtWidgets.QTableWidget(self.page_doc)
        self.tableWidget_doc.setGeometry(QtCore.QRect(0, 40, 901, 541))
        self.tableWidget_doc.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.tableWidget_doc.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_doc.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_doc.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_doc.setObjectName("tableWidget_doc")
        self.tableWidget_doc.setColumnCount(3)
        self.tableWidget_doc.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_doc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_doc.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_doc.setHorizontalHeaderItem(2, item)
        self.tableWidget_doc.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget_doc.verticalHeader().setVisible(False)
        self.pushButton_docFind = QtWidgets.QPushButton(self.page_doc)
        self.pushButton_docFind.setGeometry(QtCore.QRect(30, 0, 93, 28))
        self.pushButton_docFind.setStyleSheet("QPushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    font: 12pt \"楷体\";\n"
"    border:none;\n"
"    border-radius:7px;\n"
"    color: rgb(0, 0, 0);\n"
"}")
        self.pushButton_docFind.setObjectName("pushButton_docFind")
        self.stackedWidget.addWidget(self.page_doc)
        self.verticalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_4.addWidget(self.frame_6)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_close.clicked.connect(MainWindow.close) # type: ignore
        self.pushButton_minisize.clicked.connect(MainWindow.showMinimized) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_sup.setText(_translate("MainWindow", "采购信息管理"))
        self.pushButton_app.setText(_translate("MainWindow", "请购单信息"))
        self.pushButton_buy.setText(_translate("MainWindow", "采购单信息"))
        self.pushButton_doc.setText(_translate("MainWindow", "业务单据"))
        self.pushButton_anly.setText(_translate("MainWindow", "分析报表"))
        self.pushButton_exit.setText(_translate("MainWindow", "退出登录"))
        item = self.tableWidget_sup.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "供应商"))
        item = self.tableWidget_sup.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "供货"))
        item = self.tableWidget_sup.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "采购员"))
        item = self.tableWidget_sup.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "操作"))
        self.pushButton_supAdd.setText(_translate("MainWindow", "添加"))
        self.pushButton_supFind.setText(_translate("MainWindow", "查找"))
        self.pushButton_appAdd.setText(_translate("MainWindow", "添加"))
        item = self.tableWidget_app.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "供应商"))
        item = self.tableWidget_app.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "供货"))
        item = self.tableWidget_app.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "数量"))
        item = self.tableWidget_app.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "采购员"))
        item = self.tableWidget_app.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "申请日期"))
        item = self.tableWidget_app.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "状态"))
        item = self.tableWidget_app.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "操作"))
        self.pushButton_appFind.setText(_translate("MainWindow", "查找"))
        item = self.tableWidget_buy.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "供应商"))
        item = self.tableWidget_buy.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "货物"))
        item = self.tableWidget_buy.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "接货员"))
        item = self.tableWidget_buy.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "审核日期"))
        item = self.tableWidget_buy.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "状态"))
        item = self.tableWidget_buy.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "操作"))
        self.pushButton_appFind_2.setText(_translate("MainWindow", "查找"))
        item = self.tableWidget_anly.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "供应商"))
        item = self.tableWidget_anly.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "货物"))
        item = self.tableWidget_anly.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "采购数量"))
        item = self.tableWidget_anly.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "采购员"))
        item = self.tableWidget_anly.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "接货员"))
        item = self.tableWidget_anly.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "操作"))
        self.pushButton_anlyFind.setText(_translate("MainWindow", "查找"))
        item = self.tableWidget_doc.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "货物"))
        item = self.tableWidget_doc.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "供应商数量"))
        item = self.tableWidget_doc.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "操作"))
        self.pushButton_docFind.setText(_translate("MainWindow", "查找"))
import res_rc
