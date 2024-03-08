from model import *
from controller import *
from main import *

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QHBoxLayout, QStackedWidget, QMessageBox
from PySide6 import QtWidgets as qtw
# -*- coding: utf-8 -*-
import pymysql

# view.py
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStatusBar,
                               QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(843, 259)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(777, 16777215))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e3b\u756b\u9762", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '倉庫系統_登入畫面ypcSax.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QSizePolicy, QVBoxLayout, QWidget)


class Ui_Dialog_Main(object):
    def setupUi(self, Dialog_Main):
        if not Dialog_Main.objectName():
            Dialog_Main.setObjectName(u"Dialog_Main")
        Dialog_Main.resize(700, 300)
        self.label = QLabel(Dialog_Main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 311, 281))
        self.label.setPixmap(QPixmap(u"\u5009\u5eab\u7cfb\u7d71.png"))
        self.label.setScaledContents(True)
        self.layoutWidget = QWidget(Dialog_Main)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(370, 70, 273, 136))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_account = QLabel(self.layoutWidget)
        self.label_account.setObjectName(u"label_account")
        font = QFont()
        font.setPointSize(15)
        self.label_account.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_account)

        self.lineEdit_account = QLineEdit(self.layoutWidget)
        self.lineEdit_account.setObjectName(u"lineEdit_account")
        self.lineEdit_account.setFont(font)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lineEdit_account)

        self.verticalLayout.addLayout(self.formLayout_2)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_password = QLabel(self.layoutWidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(self.layoutWidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setFont(font)
        self.lineEdit_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_password)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(50)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.pushButton_register = QPushButton(self.layoutWidget)
        self.pushButton_register.setObjectName(u"pushButton_register")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.pushButton_register.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_register)

        self.pushButton_login = QPushButton(self.layoutWidget)
        self.pushButton_login.setObjectName(u"pushButton_login")
        self.pushButton_login.setEnabled(True)
        self.pushButton_login.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton_login)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.retranslateUi(Dialog_Main)

        QMetaObject.connectSlotsByName(Dialog_Main)

    # setupUi

    def retranslateUi(self, Dialog_Main):
        Dialog_Main.setWindowTitle(QCoreApplication.translate("Dialog_Main", u"Dialog", None))
        self.label.setText("")
        self.label_account.setText(QCoreApplication.translate("Dialog_Main", u"\u5e33\u865f\uff1a", None))
        self.label_password.setText(QCoreApplication.translate("Dialog_Main", u"\u5bc6\u78bc\uff1a", None))
        self.pushButton_register.setText(QCoreApplication.translate("Dialog_Main", u"\u8a3b\u518a", None))
        self.pushButton_login.setText(QCoreApplication.translate("Dialog_Main", u"\u767b\u5165", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '倉庫系統_註冊畫面GlseUO.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
                               QWidget)


class Ui_Dialog_2(object):
    def setupUi(self, Dialog_2):
        if not Dialog_2.objectName():
            Dialog_2.setObjectName(u"Dialog_2")
        Dialog_2.resize(700, 300)
        self.label = QLabel(Dialog_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(9, 9, 311, 281))
        self.label.setPixmap(QPixmap(u"\u5009\u5eab\u7cfb\u7d71.png"))
        self.label.setScaledContents(True)
        self.layoutWidget = QWidget(Dialog_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(351, 51, 313, 175))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_new_account = QLabel(self.layoutWidget)
        self.label_new_account.setObjectName(u"label_new_account")
        font = QFont()
        font.setPointSize(15)
        self.label_new_account.setFont(font)

        self.horizontalLayout.addWidget(self.label_new_account)

        self.lineEdit_new_account = QLineEdit(self.layoutWidget)
        self.lineEdit_new_account.setObjectName(u"lineEdit_new_account")
        self.lineEdit_new_account.setFont(font)

        self.horizontalLayout.addWidget(self.lineEdit_new_account)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_new_password = QLabel(self.layoutWidget)
        self.label_new_password.setObjectName(u"label_new_password")
        self.label_new_password.setFont(font)

        self.horizontalLayout_2.addWidget(self.label_new_password)

        self.lineEdit_new_password = QLineEdit(self.layoutWidget)
        self.lineEdit_new_password.setObjectName(u"lineEdit_new_password")
        self.lineEdit_new_password.setFont(font)
        self.lineEdit_new_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.lineEdit_new_password)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_check_password = QLabel(self.layoutWidget)
        self.label_check_password.setObjectName(u"label_check_password")
        self.label_check_password.setFont(font)

        self.horizontalLayout_3.addWidget(self.label_check_password)

        self.lineEdit_check_password = QLineEdit(self.layoutWidget)
        self.lineEdit_check_password.setObjectName(u"lineEdit_check_password")
        self.lineEdit_check_password.setFont(font)
        self.lineEdit_check_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.lineEdit_check_password)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.pushButton_return_login = QPushButton(self.layoutWidget)
        self.pushButton_return_login.setObjectName(u"pushButton_return_login")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.pushButton_return_login.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton_return_login)

        self.pushButton_register_check = QPushButton(self.layoutWidget)
        self.pushButton_register_check.setObjectName(u"pushButton_register_check")
        self.pushButton_register_check.setFont(font1)

        self.horizontalLayout_4.addWidget(self.pushButton_register_check)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog_2)

        QMetaObject.connectSlotsByName(Dialog_2)

    # setupUi

    def retranslateUi(self, Dialog_2):
        Dialog_2.setWindowTitle(QCoreApplication.translate("Dialog_2", u"Dialog", None))
        self.label.setText("")
        self.label_new_account.setText(QCoreApplication.translate("Dialog_2", u"\u65b0\u589e\u5e33\u865f\uff1a", None))
        self.label_new_password.setText(QCoreApplication.translate("Dialog_2", u"\u65b0\u589e\u5bc6\u78bc\uff1a", None))
        self.label_check_password.setText(
            QCoreApplication.translate("Dialog_2", u"\u78ba\u8a8d\u5bc6\u78bc\uff1a", None))
        self.pushButton_return_login.setText(QCoreApplication.translate("Dialog_2", u"\u8fd4\u56de\u767b\u5165", None))
        self.pushButton_register_check.setText(
            QCoreApplication.translate("Dialog_2", u"\u7533\u8acb\u8a3b\u518a", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '倉庫系統_操作畫面dDBXxw.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
                               QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QTableWidget, QTableWidgetItem, QWidget)

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '倉庫系統_操作畫面HpKUNb.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
                               QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QTableWidget, QTableWidgetItem, QWidget)



class Ui_Dialog_3(object):
    def setupUi(self, Dialog_3):
        if not Dialog_3.objectName():
            Dialog_3.setObjectName(u"Dialog_3")
        Dialog_3.resize(1000, 450)
        self.tableWidget = QTableWidget(Dialog_3)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(450, 50, 521, 192))
        self.tableWidget.setMaximumSize(QSize(600, 500))
        self.label = QLabel(Dialog_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(452, 16, 120, 25))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label.setFont(font)
        self.pushButton_search_all_item = QPushButton(Dialog_3)
        self.pushButton_search_all_item.setObjectName(u"pushButton_search_all_item")
        self.pushButton_search_all_item.setGeometry(QRect(860, 16, 104, 28))
        self.pushButton_search_all_item.setMaximumSize(QSize(120, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton_search_all_item.setFont(font1)
        self.pushButton_new_item = QPushButton(Dialog_3)
        self.pushButton_new_item.setObjectName(u"pushButton_new_item")
        self.pushButton_new_item.setGeometry(QRect(19, 110, 75, 28))
        self.pushButton_new_item.setMaximumSize(QSize(100, 30))
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.pushButton_new_item.setFont(font2)
        self.label_5 = QLabel(Dialog_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(129, 45, 45, 25))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(Dialog_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(295, 45, 45, 25))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(Dialog_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(237, 45, 45, 25))
        self.label_7.setFont(font1)
        self.label_3 = QLabel(Dialog_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(19, 150, 120, 25))
        self.label_3.setFont(font)
        self.label_8 = QLabel(Dialog_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(79, 183, 45, 25))
        self.label_8.setFont(font1)
        self.pushButton_update_item = QPushButton(Dialog_3)
        self.pushButton_update_item.setObjectName(u"pushButton_update_item")
        self.pushButton_update_item.setGeometry(QRect(19, 248, 75, 28))
        self.pushButton_update_item.setMaximumSize(QSize(100, 30))
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.pushButton_update_item.setFont(font3)
        self.label_9 = QLabel(Dialog_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(353, 183, 45, 25))
        self.label_9.setFont(font1)
        self.label_10 = QLabel(Dialog_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(295, 183, 45, 25))
        self.label_10.setFont(font1)
        self.label_11 = QLabel(Dialog_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(187, 183, 45, 25))
        self.label_11.setFont(font1)
        self.label_12 = QLabel(Dialog_3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(21, 183, 26, 25))
        self.label_12.setFont(font1)
        self.pushButton_del_item = QPushButton(Dialog_3)
        self.pushButton_del_item.setObjectName(u"pushButton_del_item")
        self.pushButton_del_item.setGeometry(QRect(19, 386, 75, 28))
        self.pushButton_del_item.setMaximumSize(QSize(100, 30))
        self.pushButton_del_item.setFont(font3)
        self.label_13 = QLabel(Dialog_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(187, 321, 45, 25))
        self.label_13.setFont(font1)
        self.label_14 = QLabel(Dialog_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(79, 321, 45, 25))
        self.label_14.setFont(font1)
        self.label_15 = QLabel(Dialog_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(21, 321, 26, 25))
        self.label_15.setFont(font1)
        self.label_16 = QLabel(Dialog_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(19, 288, 371, 25))
        self.label_16.setFont(font)
        self.pushButton_search_item = QPushButton(Dialog_3)
        self.pushButton_search_item.setObjectName(u"pushButton_search_item")
        self.pushButton_search_item.setGeometry(QRect(449, 391, 75, 27))
        self.pushButton_search_item.setMaximumSize(QSize(100, 30))
        self.pushButton_search_item.setFont(font3)
        self.label_17 = QLabel(Dialog_3)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(450, 324, 26, 25))
        self.label_17.setFont(font1)
        self.label_18 = QLabel(Dialog_3)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(616, 324, 45, 25))
        self.label_18.setFont(font1)
        self.label_19 = QLabel(Dialog_3)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(448, 291, 371, 25))
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"")
        self.label_19.setFrameShape(QFrame.NoFrame)
        self.label_19.setFrameShadow(QFrame.Plain)
        self.label_19.setLineWidth(1)
        self.label_19.setWordWrap(False)
        self.label_20 = QLabel(Dialog_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(508, 324, 45, 25))
        self.label_20.setFont(font1)
        self.lineEdit_new_name = QLineEdit(Dialog_3)
        self.lineEdit_new_name.setObjectName(u"lineEdit_new_name")
        self.lineEdit_new_name.setGeometry(QRect(21, 76, 100, 26))
        self.lineEdit_new_name.setMaximumSize(QSize(100, 30))
        self.lineEdit_new_name.setBaseSize(QSize(0, 0))
        self.lineEdit_new_name.setFont(font1)
        self.lineEdit_new_firm = QLineEdit(Dialog_3)
        self.lineEdit_new_firm.setObjectName(u"lineEdit_new_firm")
        self.lineEdit_new_firm.setGeometry(QRect(129, 76, 100, 26))
        self.lineEdit_new_firm.setMaximumSize(QSize(100, 30))
        self.lineEdit_new_firm.setFont(font1)
        self.lineEdit_new_amount = QLineEdit(Dialog_3)
        self.lineEdit_new_amount.setObjectName(u"lineEdit_new_amount")
        self.lineEdit_new_amount.setGeometry(QRect(295, 76, 50, 26))
        self.lineEdit_new_amount.setMaximumSize(QSize(50, 30))
        self.lineEdit_new_amount.setFont(font1)
        self.lineEdit_new_price = QLineEdit(Dialog_3)
        self.lineEdit_new_price.setObjectName(u"lineEdit_new_price")
        self.lineEdit_new_price.setGeometry(QRect(237, 76, 50, 26))
        self.lineEdit_new_price.setMaximumSize(QSize(50, 30))
        self.lineEdit_new_price.setFont(font1)
        self.lineEdit_update_price = QLineEdit(Dialog_3)
        self.lineEdit_update_price.setObjectName(u"lineEdit_update_price")
        self.lineEdit_update_price.setGeometry(QRect(295, 214, 50, 26))
        self.lineEdit_update_price.setMaximumSize(QSize(50, 30))
        self.lineEdit_update_price.setFont(font1)
        self.lineEdit_update_amount = QLineEdit(Dialog_3)
        self.lineEdit_update_amount.setObjectName(u"lineEdit_update_amount")
        self.lineEdit_update_amount.setGeometry(QRect(353, 214, 50, 26))
        self.lineEdit_update_amount.setMaximumSize(QSize(50, 30))
        self.lineEdit_update_amount.setFont(font1)
        self.lineEdit_del_id = QLineEdit(Dialog_3)
        self.lineEdit_del_id.setObjectName(u"lineEdit_del_id")
        self.lineEdit_del_id.setGeometry(QRect(21, 352, 50, 26))
        self.lineEdit_del_id.setMaximumSize(QSize(50, 30))
        self.lineEdit_del_id.setFont(font1)
        self.lineEdit_del_id.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        self.lineEdit_update_id = QLineEdit(Dialog_3)
        self.lineEdit_update_id.setObjectName(u"lineEdit_update_id")
        self.lineEdit_update_id.setGeometry(QRect(21, 214, 50, 26))
        self.lineEdit_update_id.setMaximumSize(QSize(50, 30))
        self.lineEdit_update_id.setFont(font1)
        self.lineEdit_search_id = QLineEdit(Dialog_3)
        self.lineEdit_search_id.setObjectName(u"lineEdit_search_id")
        self.lineEdit_search_id.setGeometry(QRect(450, 355, 50, 26))
        self.lineEdit_search_id.setMaximumSize(QSize(50, 30))
        self.lineEdit_search_id.setFont(font1)
        self.lineEdit_update_name = QLineEdit(Dialog_3)
        self.lineEdit_update_name.setObjectName(u"lineEdit_update_name")
        self.lineEdit_update_name.setGeometry(QRect(79, 214, 100, 26))
        self.lineEdit_update_name.setMaximumSize(QSize(100, 30))
        self.lineEdit_update_name.setFont(font1)
        self.lineEdit_update_firm = QLineEdit(Dialog_3)
        self.lineEdit_update_firm.setObjectName(u"lineEdit_update_firm")
        self.lineEdit_update_firm.setGeometry(QRect(187, 214, 100, 26))
        self.lineEdit_update_firm.setMaximumSize(QSize(100, 30))
        self.lineEdit_update_firm.setFont(font1)
        self.lineEdit_del_name = QLineEdit(Dialog_3)
        self.lineEdit_del_name.setObjectName(u"lineEdit_del_name")
        self.lineEdit_del_name.setGeometry(QRect(79, 352, 100, 26))
        self.lineEdit_del_name.setMaximumSize(QSize(100, 30))
        self.lineEdit_del_name.setFont(font1)
        self.lineEdit_del_firm = QLineEdit(Dialog_3)
        self.lineEdit_del_firm.setObjectName(u"lineEdit_del_firm")
        self.lineEdit_del_firm.setGeometry(QRect(187, 352, 100, 26))
        self.lineEdit_del_firm.setMaximumSize(QSize(100, 30))
        self.lineEdit_del_firm.setFont(font1)
        self.lineEdit_search_name = QLineEdit(Dialog_3)
        self.lineEdit_search_name.setObjectName(u"lineEdit_search_name")
        self.lineEdit_search_name.setGeometry(QRect(508, 355, 100, 26))
        self.lineEdit_search_name.setMaximumSize(QSize(100, 30))
        self.lineEdit_search_name.setFont(font1)
        self.lineEdit_search_firm = QLineEdit(Dialog_3)
        self.lineEdit_search_firm.setObjectName(u"lineEdit_search_firm")
        self.lineEdit_search_firm.setGeometry(QRect(616, 355, 100, 26))
        self.lineEdit_search_firm.setMaximumSize(QSize(100, 30))
        self.lineEdit_search_firm.setFont(font1)
        self.pushButton_return_login = QPushButton(Dialog_3)
        self.pushButton_return_login.setObjectName(u"pushButton_return_login")
        self.pushButton_return_login.setGeometry(QRect(767, 392, 100, 30))
        self.pushButton_return_login.setMinimumSize(QSize(100, 30))
        self.pushButton_return_login.setMaximumSize(QSize(100, 30))
        self.pushButton_return_login.setFont(font)
        self.label_2 = QLabel(Dialog_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(19, 12, 120, 25))
        self.label_2.setFont(font)
        self.label_4 = QLabel(Dialog_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(21, 45, 45, 25))
        self.label_4.setFont(font1)
        self.label_21 = QLabel(Dialog_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(440, 10, 541, 421))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"background:#9D9D9D")
        self.label_21.setFrameShape(QFrame.NoFrame)
        self.label_21.setFrameShadow(QFrame.Plain)
        self.label_21.setLineWidth(1)
        self.label_21.setWordWrap(False)
        self.pushButton_order = QPushButton(Dialog_3)
        self.pushButton_order.setObjectName(u"pushButton_order")
        self.pushButton_order.setGeometry(QRect(873, 392, 100, 30))
        self.pushButton_order.setMinimumSize(QSize(100, 30))
        self.pushButton_order.setMaximumSize(QSize(100, 30))
        self.pushButton_order.setFont(font)
        self.label_21.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.pushButton_search_all_item.raise_()
        self.pushButton_new_item.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_3.raise_()
        self.label_8.raise_()
        self.pushButton_update_item.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.pushButton_del_item.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.pushButton_search_item.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.lineEdit_new_name.raise_()
        self.lineEdit_new_firm.raise_()
        self.lineEdit_new_amount.raise_()
        self.lineEdit_new_price.raise_()
        self.lineEdit_update_price.raise_()
        self.lineEdit_update_amount.raise_()
        self.lineEdit_del_id.raise_()
        self.lineEdit_update_id.raise_()
        self.lineEdit_search_id.raise_()
        self.lineEdit_update_name.raise_()
        self.lineEdit_update_firm.raise_()
        self.lineEdit_del_name.raise_()
        self.lineEdit_del_firm.raise_()
        self.lineEdit_search_name.raise_()
        self.lineEdit_search_firm.raise_()
        self.pushButton_return_login.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.pushButton_order.raise_()
        QWidget.setTabOrder(self.lineEdit_new_name, self.lineEdit_new_firm)
        QWidget.setTabOrder(self.lineEdit_new_firm, self.lineEdit_new_price)
        QWidget.setTabOrder(self.lineEdit_new_price, self.lineEdit_new_amount)
        QWidget.setTabOrder(self.lineEdit_new_amount, self.pushButton_new_item)
        QWidget.setTabOrder(self.pushButton_new_item, self.lineEdit_update_id)
        QWidget.setTabOrder(self.lineEdit_update_id, self.lineEdit_update_name)
        QWidget.setTabOrder(self.lineEdit_update_name, self.lineEdit_update_firm)
        QWidget.setTabOrder(self.lineEdit_update_firm, self.lineEdit_update_price)
        QWidget.setTabOrder(self.lineEdit_update_price, self.lineEdit_update_amount)
        QWidget.setTabOrder(self.lineEdit_update_amount, self.pushButton_update_item)
        QWidget.setTabOrder(self.pushButton_update_item, self.lineEdit_del_id)
        QWidget.setTabOrder(self.lineEdit_del_id, self.lineEdit_del_name)
        QWidget.setTabOrder(self.lineEdit_del_name, self.lineEdit_del_firm)
        QWidget.setTabOrder(self.lineEdit_del_firm, self.pushButton_del_item)
        QWidget.setTabOrder(self.pushButton_del_item, self.lineEdit_search_id)
        QWidget.setTabOrder(self.lineEdit_search_id, self.lineEdit_search_name)
        QWidget.setTabOrder(self.lineEdit_search_name, self.lineEdit_search_firm)
        QWidget.setTabOrder(self.lineEdit_search_firm, self.pushButton_search_item)
        QWidget.setTabOrder(self.pushButton_search_item, self.pushButton_return_login)
        QWidget.setTabOrder(self.pushButton_return_login, self.pushButton_search_all_item)
        QWidget.setTabOrder(self.pushButton_search_all_item, self.tableWidget)

        self.retranslateUi(Dialog_3)

        QMetaObject.connectSlotsByName(Dialog_3)

    # setupUi

    def retranslateUi(self, Dialog_3):
        Dialog_3.setWindowTitle(QCoreApplication.translate("Dialog_3", u"Dialog", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog_3", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog_3", u"\u5546\u54c1", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog_3", u"\u5ee0\u5546", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog_3", u"\u55ae\u50f9", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog_3", u"\u6578\u91cf", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog_3", u"1", None));
        self.label.setText(QCoreApplication.translate("Dialog_3", u"\u5009\u5eab\u641c\u5c0b\u5217\u8868", None))
        self.pushButton_search_all_item.setText(
            QCoreApplication.translate("Dialog_3", u"\u5217\u51fa\u6240\u6709\u54c1\u9805", None))
        self.pushButton_new_item.setText(QCoreApplication.translate("Dialog_3", u"\u65b0\u589e\u54c1\u9805", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_3", u"\u5ee0\u5546:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_3", u"\u6578\u91cf:", None))
        self.label_7.setText(QCoreApplication.translate("Dialog_3", u"\u55ae\u50f9:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_3", u"\u66f4\u65b0\u54c1\u9805\u8cc7\u6599", None))
        self.label_8.setText(QCoreApplication.translate("Dialog_3", u"\u5546\u54c1:", None))
        self.pushButton_update_item.setText(QCoreApplication.translate("Dialog_3", u"\u66f4\u65b0\u54c1\u9805", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_3", u"\u6578\u91cf:", None))
        self.label_10.setText(QCoreApplication.translate("Dialog_3", u"\u55ae\u50f9:", None))
        self.label_11.setText(QCoreApplication.translate("Dialog_3", u"\u5ee0\u5546:", None))
        self.label_12.setText(QCoreApplication.translate("Dialog_3", u"ID:", None))
        self.pushButton_del_item.setText(QCoreApplication.translate("Dialog_3", u"\u522a\u9664\u54c1\u9805", None))
        self.label_13.setText(QCoreApplication.translate("Dialog_3", u"\u5ee0\u5546:", None))
        self.label_14.setText(QCoreApplication.translate("Dialog_3", u"\u5546\u54c1:", None))
        self.label_15.setText(QCoreApplication.translate("Dialog_3", u"ID:", None))
        self.label_16.setText(QCoreApplication.translate("Dialog_3",
                                                         u"\u522a\u9664\u54c1\u9805\u8cc7\u6599 (\u4f9dID/\u5546\u54c1/\u5ee0\u5546 \u64c7\u4e00\u586b\u5beb)",
                                                         None))
        self.pushButton_search_item.setText(QCoreApplication.translate("Dialog_3", u"\u641c\u5c0b\u54c1\u9805", None))
        self.label_17.setText(QCoreApplication.translate("Dialog_3", u"ID:", None))
        self.label_18.setText(QCoreApplication.translate("Dialog_3", u"\u5ee0\u5546:", None))
        self.label_19.setText(QCoreApplication.translate("Dialog_3",
                                                         u"\u641c\u5c0b\u54c1\u9805\u8cc7\u6599 (\u4f9dID/\u5546\u54c1/\u5ee0\u5546 \u64c7\u4e00\u586b\u5beb)",
                                                         None))
        self.label_20.setText(QCoreApplication.translate("Dialog_3", u"\u5546\u54c1:", None))
        self.pushButton_return_login.setText(QCoreApplication.translate("Dialog_3", u"\u8fd4\u56de\u767b\u5165", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_3", u"\u65b0\u589e\u54c1\u9805\u8cc7\u6599", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_3", u"\u5546\u54c1:", None))
        self.label_21.setText("")
        self.pushButton_order.setText(QCoreApplication.translate("Dialog_3", u"\u8a02\u55ae\u7cfb\u7d71", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file '倉庫系統_訂單畫面PXOKrF.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHeaderView,
                               QLabel, QLineEdit, QPushButton, QSizePolicy,
                               QTableWidget, QTableWidgetItem, QWidget)


class Ui_Dialog_4(object):
    def setupUi(self, Dialog_4):
        if not Dialog_4.objectName():
            Dialog_4.setObjectName(u"Dialog_4")
        Dialog_4.resize(1000, 450)
        self.tableWidget = QTableWidget(Dialog_4)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(21, 41, 450, 200))
        self.tableWidget.setMinimumSize(QSize(450, 200))
        self.tableWidget.setMaximumSize(QSize(450, 200))
        self.tableWidget_2 = QTableWidget(Dialog_4)
        if (self.tableWidget_2.columnCount() < 4):
            self.tableWidget_2.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        if (self.tableWidget_2.rowCount() < 1):
            self.tableWidget_2.setRowCount(1)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem9)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(526, 41, 450, 200))
        self.tableWidget_2.setMinimumSize(QSize(450, 200))
        self.tableWidget_2.setMaximumSize(QSize(450, 200))
        self.label_22 = QLabel(Dialog_4)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(20, 10, 120, 25))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_23 = QLabel(Dialog_4)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(530, 10, 191, 25))
        self.label_23.setFont(font)
        self.pushButton_search_all_order = QPushButton(Dialog_4)
        self.pushButton_search_all_order.setObjectName(u"pushButton_search_all_order")
        self.pushButton_search_all_order.setGeometry(QRect(365, 10, 104, 28))
        self.pushButton_search_all_order.setMaximumSize(QSize(120, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.pushButton_search_all_order.setFont(font1)
        self.label_7 = QLabel(Dialog_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(238, 269, 71, 25))
        self.label_7.setFont(font1)
        self.label_5 = QLabel(Dialog_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(130, 269, 101, 25))
        self.label_5.setFont(font1)
        self.label_2 = QLabel(Dialog_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 246, 120, 25))
        self.label_2.setFont(font)
        self.lineEdit_new_order_name = QLineEdit(Dialog_4)
        self.lineEdit_new_order_name.setObjectName(u"lineEdit_new_order_name")
        self.lineEdit_new_order_name.setGeometry(QRect(22, 300, 100, 26))
        self.lineEdit_new_order_name.setMaximumSize(QSize(100, 30))
        self.lineEdit_new_order_name.setBaseSize(QSize(0, 0))
        self.lineEdit_new_order_name.setFont(font1)
        self.lineEdit_new_order_item_id = QLineEdit(Dialog_4)
        self.lineEdit_new_order_item_id.setObjectName(u"lineEdit_new_order_item_id")
        self.lineEdit_new_order_item_id.setGeometry(QRect(130, 300, 100, 26))
        self.lineEdit_new_order_item_id.setMaximumSize(QSize(100, 30))
        self.lineEdit_new_order_item_id.setFont(font1)
        self.lineEdit_new_order_amount = QLineEdit(Dialog_4)
        self.lineEdit_new_order_amount.setObjectName(u"lineEdit_new_order_amount")
        self.lineEdit_new_order_amount.setGeometry(QRect(238, 300, 70, 26))
        self.lineEdit_new_order_amount.setMaximumSize(QSize(70, 30))
        self.lineEdit_new_order_amount.setFont(font1)
        self.label_4 = QLabel(Dialog_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(22, 269, 71, 25))
        self.label_4.setFont(font1)
        self.pushButton_new_order = QPushButton(Dialog_4)
        self.pushButton_new_order.setObjectName(u"pushButton_new_order")
        self.pushButton_new_order.setGeometry(QRect(320, 299, 75, 28))
        self.pushButton_new_order.setMaximumSize(QSize(100, 30))
        font2 = QFont()
        font2.setFamilies([u"Microsoft JhengHei UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.pushButton_new_order.setFont(font2)
        self.label_6 = QLabel(Dialog_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(22, 368, 71, 25))
        self.label_6.setFont(font1)
        self.lineEdit_del_order_name = QLineEdit(Dialog_4)
        self.lineEdit_del_order_name.setObjectName(u"lineEdit_del_order_name")
        self.lineEdit_del_order_name.setGeometry(QRect(130, 399, 100, 26))
        self.lineEdit_del_order_name.setMaximumSize(QSize(100, 30))
        self.lineEdit_del_order_name.setFont(font1)
        self.label_3 = QLabel(Dialog_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 345, 120, 25))
        self.label_3.setFont(font)
        self.label_8 = QLabel(Dialog_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 368, 101, 25))
        self.label_8.setFont(font1)
        self.pushButton_del_order = QPushButton(Dialog_4)
        self.pushButton_del_order.setObjectName(u"pushButton_del_order")
        self.pushButton_del_order.setGeometry(QRect(240, 398, 75, 28))
        self.pushButton_del_order.setMaximumSize(QSize(100, 30))
        self.pushButton_del_order.setFont(font2)
        self.lineEdit_del_order_id = QLineEdit(Dialog_4)
        self.lineEdit_del_order_id.setObjectName(u"lineEdit_del_order_id")
        self.lineEdit_del_order_id.setGeometry(QRect(22, 399, 100, 26))
        self.lineEdit_del_order_id.setMaximumSize(QSize(100, 30))
        self.lineEdit_del_order_id.setBaseSize(QSize(0, 0))
        self.lineEdit_del_order_id.setFont(font1)
        self.label_9 = QLabel(Dialog_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(530, 269, 71, 25))
        self.label_9.setFont(font1)
        self.lineEdit_search_order_id = QLineEdit(Dialog_4)
        self.lineEdit_search_order_id.setObjectName(u"lineEdit_search_order_id")
        self.lineEdit_search_order_id.setGeometry(QRect(638, 300, 100, 26))
        self.lineEdit_search_order_id.setMaximumSize(QSize(100, 30))
        self.lineEdit_search_order_id.setFont(font1)
        self.label_10 = QLabel(Dialog_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(528, 246, 191, 25))
        self.label_10.setFont(font)
        self.label_11 = QLabel(Dialog_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(638, 269, 101, 25))
        self.label_11.setFont(font1)
        self.pushButton_search_special_order = QPushButton(Dialog_4)
        self.pushButton_search_special_order.setObjectName(u"pushButton_search_special_order")
        self.pushButton_search_special_order.setGeometry(QRect(750, 299, 120, 28))
        self.pushButton_search_special_order.setMaximumSize(QSize(120, 30))
        self.pushButton_search_special_order.setFont(font2)
        self.lineEdit_search_order_name = QLineEdit(Dialog_4)
        self.lineEdit_search_order_name.setObjectName(u"lineEdit_search_order_name")
        self.lineEdit_search_order_name.setGeometry(QRect(530, 300, 100, 26))
        self.lineEdit_search_order_name.setMaximumSize(QSize(100, 30))
        self.lineEdit_search_order_name.setBaseSize(QSize(0, 0))
        self.lineEdit_search_order_name.setFont(font1)
        self.pushButton_search_all_order_item = QPushButton(Dialog_4)
        self.pushButton_search_all_order_item.setObjectName(u"pushButton_search_all_order_item")
        self.pushButton_search_all_order_item.setGeometry(QRect(853, 10, 121, 28))
        self.pushButton_search_all_order_item.setMaximumSize(QSize(150, 30))
        self.pushButton_search_all_order_item.setFont(font1)
        self.label_21 = QLabel(Dialog_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(510, 7, 481, 431))
        self.label_21.setFont(font)
        self.label_21.setStyleSheet(u"background:#9D9D9D")
        self.label_21.setFrameShape(QFrame.NoFrame)
        self.label_21.setFrameShadow(QFrame.Plain)
        self.label_21.setLineWidth(1)
        self.label_21.setWordWrap(False)
        self.pushButton_goto_warehouse = QPushButton(Dialog_4)
        self.pushButton_goto_warehouse.setObjectName(u"pushButton_goto_warehouse")
        self.pushButton_goto_warehouse.setGeometry(QRect(886, 400, 100, 30))
        self.pushButton_goto_warehouse.setMinimumSize(QSize(100, 30))
        self.pushButton_goto_warehouse.setMaximumSize(QSize(100, 30))
        self.pushButton_goto_warehouse.setFont(font)
        self.pushButton_return_login = QPushButton(Dialog_4)
        self.pushButton_return_login.setObjectName(u"pushButton_return_login")
        self.pushButton_return_login.setGeometry(QRect(780, 400, 100, 30))
        self.pushButton_return_login.setMinimumSize(QSize(100, 30))
        self.pushButton_return_login.setMaximumSize(QSize(100, 30))
        self.pushButton_return_login.setFont(font)
        self.label_21.raise_()
        self.tableWidget.raise_()
        self.tableWidget_2.raise_()
        self.label_22.raise_()
        self.label_23.raise_()
        self.pushButton_search_all_order.raise_()
        self.label_7.raise_()
        self.label_5.raise_()
        self.label_2.raise_()
        self.lineEdit_new_order_name.raise_()
        self.lineEdit_new_order_item_id.raise_()
        self.lineEdit_new_order_amount.raise_()
        self.label_4.raise_()
        self.pushButton_new_order.raise_()
        self.label_6.raise_()
        self.lineEdit_del_order_name.raise_()
        self.label_3.raise_()
        self.label_8.raise_()
        self.pushButton_del_order.raise_()
        self.lineEdit_del_order_id.raise_()
        self.label_9.raise_()
        self.lineEdit_search_order_id.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.pushButton_search_special_order.raise_()
        self.lineEdit_search_order_name.raise_()
        self.pushButton_search_all_order_item.raise_()
        self.pushButton_goto_warehouse.raise_()
        self.pushButton_return_login.raise_()
        QWidget.setTabOrder(self.lineEdit_new_order_name, self.lineEdit_new_order_item_id)
        QWidget.setTabOrder(self.lineEdit_new_order_item_id, self.lineEdit_new_order_amount)
        QWidget.setTabOrder(self.lineEdit_new_order_amount, self.pushButton_new_order)
        QWidget.setTabOrder(self.pushButton_new_order, self.lineEdit_del_order_id)
        QWidget.setTabOrder(self.lineEdit_del_order_id, self.lineEdit_del_order_name)
        QWidget.setTabOrder(self.lineEdit_del_order_name, self.pushButton_del_order)
        QWidget.setTabOrder(self.pushButton_del_order, self.lineEdit_search_order_name)
        QWidget.setTabOrder(self.lineEdit_search_order_name, self.lineEdit_search_order_id)
        QWidget.setTabOrder(self.lineEdit_search_order_id, self.pushButton_search_special_order)
        QWidget.setTabOrder(self.pushButton_search_special_order, self.pushButton_search_all_order)
        QWidget.setTabOrder(self.pushButton_search_all_order, self.pushButton_search_all_order_item)
        QWidget.setTabOrder(self.pushButton_search_all_order_item, self.pushButton_return_login)
        QWidget.setTabOrder(self.pushButton_return_login, self.pushButton_goto_warehouse)
        QWidget.setTabOrder(self.pushButton_goto_warehouse, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.tableWidget_2)

        self.retranslateUi(Dialog_4)

        QMetaObject.connectSlotsByName(Dialog_4)

    # setupUi

    def retranslateUi(self, Dialog_4):
        Dialog_4.setWindowTitle(QCoreApplication.translate("Dialog_4", u"Dialog", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55aeID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u5ba2\u6236", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u54c1\u9805ID", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u6578\u91cf", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog_4", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u5ba2\u6236", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u54c1\u9805", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u6578\u91cf", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog_4", u"\u5eab\u5b58\u6578\u91cf", None));
        ___qtablewidgetitem9 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dialog_4", u"1", None));
        self.label_22.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u5217\u8868", None))
        self.label_23.setText(
            QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u548c\u54c1\u9805\u641c\u5c0b\u5217\u8868", None))
        self.pushButton_search_all_order.setText(
            QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u5217\u8868\u66f4\u65b0", None))
        self.label_7.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u6578\u91cf:", None))
        self.label_5.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u54c1\u9805ID:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog_4", u"\u65b0\u589e\u8a02\u55ae\u8cc7\u6599", None))
        self.label_4.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u5ba2\u6236:", None))
        self.pushButton_new_order.setText(QCoreApplication.translate("Dialog_4", u"\u65b0\u589e\u8a02\u55ae", None))
        self.label_6.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55aeID", None))
        self.label_3.setText(QCoreApplication.translate("Dialog_4", u"\u522a\u9664\u8a02\u55ae\u8cc7\u6599", None))
        self.label_8.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u5ba2\u6236:", None))
        self.pushButton_del_order.setText(QCoreApplication.translate("Dialog_4", u"\u522a\u9664\u8a02\u55ae", None))
        self.label_9.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u5ba2\u6236:", None))
        self.label_10.setText(
            QCoreApplication.translate("Dialog_4", u"\u641c\u5c0b\u8a02\u55ae\u548c\u54c1\u9805\u8cc7\u6599", None))
        self.label_11.setText(QCoreApplication.translate("Dialog_4", u"\u8a02\u55ae\u54c1\u9805ID:", None))
        self.pushButton_search_special_order.setText(
            QCoreApplication.translate("Dialog_4", u"\u6307\u5b9a\u641c\u5c0b\u8a02\u55ae", None))
        self.pushButton_search_all_order_item.setText(
            QCoreApplication.translate("Dialog_4", u"\u5168\u90e8\u8a02\u55ae\u641c\u5c0b", None))
        self.label_21.setText("")
        self.pushButton_goto_warehouse.setText(
            QCoreApplication.translate("Dialog_4", u"\u5009\u5eab\u7cfb\u7d71", None))
        self.pushButton_return_login.setText(QCoreApplication.translate("Dialog_4", u"\u8fd4\u56de\u767b\u5165", None))
    # retranslateUi
