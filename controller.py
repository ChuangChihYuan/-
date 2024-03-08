from model import *
from view import *
from main import *

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QHBoxLayout, QStackedWidget, QMessageBox
from PySide6 import QtWidgets as qtw
# -*- coding: utf-8 -*-
import pymysql

from PySide6.QtWidgets import QWidget

# comtroller.py
class Dialog_Login(qtw.QWidget, Ui_Dialog_Main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Dialog_Register(qtw.QWidget, Ui_Dialog_2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Dialog_Operate(qtw.QWidget, Ui_Dialog_3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Dialog_Order(qtw.QWidget, Ui_Dialog_4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        # 資料庫
        self.user_model = UserModel()
        # get_data = self.user_model.load_data()
        # print(f"load_data:{get_data}")

        # 繼承UI MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stacked_widget = qtw.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # 繼承UI畫面和元件
        self.dialog_login = Dialog_Login()
        self.dialog_register = Dialog_Register()
        self.dialog_operate = Dialog_Operate()
        self.dialog_order = Dialog_Order()
        # self.form1_qtw = qtw.QWidget()
        # self.form1_ui = Ui_Dialog1()
        # self.form1_ui.setupUi(self.form1_qtw)

        # 增加畫面
        self.stacked_widget.addWidget(self.dialog_login)
        self.stacked_widget.addWidget(self.dialog_register)
        self.stacked_widget.addWidget(self.dialog_operate)
        self.stacked_widget.addWidget(self.dialog_order)

        # dialog_login 按鈕
        self.dialog_login.pushButton_login.clicked.connect(self.on_login)
        self.dialog_login.pushButton_register.clicked.connect(self.show_register_window)

        # dialog_register 按鈕
        self.dialog_register.pushButton_register_check.clicked.connect(self.on_register)
        self.dialog_register.pushButton_return_login.clicked.connect(self.show_login_window)

        # dialog_operate 按鈕
        self.dialog_operate.pushButton_return_login.clicked.connect(self.show_login_window)
        self.dialog_operate.pushButton_search_all_item.clicked.connect(self.load_data)

        self.dialog_operate.pushButton_new_item.clicked.connect(self.new_item)

        self.dialog_operate.pushButton_update_item.clicked.connect(self.update_item)

        self.dialog_operate.pushButton_del_item.clicked.connect(self.delete_item)

        self.dialog_operate.pushButton_search_item.clicked.connect(self.search_item)

        self.dialog_operate.pushButton_order.clicked.connect(self.show_order_window)

        # dialog_order 按鈕
        self.dialog_order.pushButton_goto_warehouse.clicked.connect(self.show_operate_window)
        self.dialog_order.pushButton_return_login.clicked.connect(self.show_login_window)

        self.dialog_order.pushButton_search_all_order.clicked.connect(self.search_all_order)
        self.dialog_order.pushButton_search_all_order_item.clicked.connect(self.search_all_order_item)

        self.dialog_order.pushButton_new_order.clicked.connect(self.new_order)
        self.dialog_order.pushButton_del_order.clicked.connect(self.delete_order)
        self.dialog_order.pushButton_search_special_order.clicked.connect(self.search_special_order)

        self.show_login_window()

    def new_order(self):
        new_order_name = self.dialog_order.lineEdit_new_order_name.text()
        new_order_item_id = self.dialog_order.lineEdit_new_order_item_id.text()
        new_order_item_amount = self.dialog_order.lineEdit_new_order_amount.text()

        if not new_order_name or not new_order_item_id or not new_order_item_amount:
            QMessageBox.critical(self, '新增訂單失敗', '尚有欄位未填寫！')
            return

        if new_order_item_id.isdigit() != True:
            QMessageBox.critical(self, '新增訂單失敗', '訂單品項ID只能填數字！')
            return

        if new_order_item_amount.isdigit() != True:
            QMessageBox.critical(self, '新增訂單失敗', '訂單數量只能填數字！')
            return

        self.user_model.new_order(new_order_name, new_order_item_id, new_order_item_amount)
        QMessageBox.information(self, '新增訂單成功', '新增訂單成功！')

    def delete_order(self):
        delete_order_id = self.dialog_order.lineEdit_del_order_id.text()
        delete_order_name = self.dialog_order.lineEdit_del_order_name.text()

        if not delete_order_id and not delete_order_name:
            print(f"刪除訂單失敗")
            QMessageBox.critical(self, '刪除訂單失敗', '請填寫其中一個欄位！')
            return
        else:
            if self.user_model.search_order_id(delete_order_id) != True and delete_order_id:
                QMessageBox.critical(self, '刪除訂單失敗', '沒有找到此訂單ID！')
                return
            if self.user_model.search_order_name(delete_order_name) != True and delete_order_name:
                QMessageBox.critical(self, '刪除訂單失敗', '沒有找到此訂單客戶！')
                return

            self.user_model.delete_order(delete_order_id, delete_order_name)
            QMessageBox.information(self, '刪除訂單成功', '刪除訂單成功！')

    def search_special_order(self):
        search_order_name = self.dialog_order.lineEdit_search_order_name.text()
        search_order_item_id = self.dialog_order.lineEdit_search_order_id.text()

        if not search_order_name and not search_order_item_id:
            print(f"搜尋訂單和品項失敗")
            QMessageBox.critical(self, '搜尋訂單和品項失敗', '請填寫其中一個欄位！')
            return
        else:
            if self.user_model.search_order_name(search_order_name) != True and search_order_name:
                QMessageBox.critical(self, '搜尋訂單和品項失敗', '沒有找到此訂單客戶！')
                return
            if self.user_model.search_order_item_id(search_order_item_id) != True and search_order_item_id:
                QMessageBox.critical(self, '搜尋訂單和品項失敗', '沒有找到此訂單品項ID！')
                return

            items_data = self.user_model.search_special_order(search_order_name, search_order_item_id)

            print(f"items_data: {items_data}")
            row = 0

            self.dialog_order.tableWidget_2.setRowCount(len(items_data))
            print(f"len:{len(items_data)}")

            for item in items_data:
                # Create QTableWidgetItems for each value
                order_name = QTableWidgetItem(str(item[0]))
                item_name = QTableWidgetItem(str(item[1]))
                order_item_amount = QTableWidgetItem(str(item[2]))
                item_amount = QTableWidgetItem(str(item[3]))

                # Set the flags and alignment
                order_name.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                item_name.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                order_item_amount.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                item_amount.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

                order_name.setTextAlignment(Qt.AlignCenter)
                item_name.setTextAlignment(Qt.AlignCenter)
                order_item_amount.setTextAlignment(Qt.AlignCenter)
                item_amount.setTextAlignment(Qt.AlignCenter)

                # Set the items in the table
                self.dialog_order.tableWidget_2.setItem(row, 0, order_name)
                self.dialog_order.tableWidget_2.setItem(row, 1, item_name)
                self.dialog_order.tableWidget_2.setItem(row, 2, order_item_amount)
                self.dialog_order.tableWidget_2.setItem(row, 3, item_amount)

                row += 1

            QMessageBox.information(self, '搜尋訂單和品項成功', '搜尋訂單和品項成功！')

    def search_all_order_item(self):
        items_data = self.user_model.load_order_item_data()

        print(f"items_data: {items_data}")
        row = 0

        self.dialog_order.tableWidget_2.setRowCount(len(items_data))
        print(f"len:{len(items_data)}")

        for item in items_data:
            # Create QTableWidgetItems for each value
            order_name = QTableWidgetItem(str(item[0]))
            item_name = QTableWidgetItem(str(item[1]))
            order_item_amount = QTableWidgetItem(str(item[2]))
            item_amount = QTableWidgetItem(str(item[3]))

            # Set the flags and alignment
            order_name.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item_name.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            order_item_amount.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item_amount.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

            order_name.setTextAlignment(Qt.AlignCenter)
            item_name.setTextAlignment(Qt.AlignCenter)
            order_item_amount.setTextAlignment(Qt.AlignCenter)
            item_amount.setTextAlignment(Qt.AlignCenter)

            # Set the items in the table
            self.dialog_order.tableWidget_2.setItem(row, 0, order_name)
            self.dialog_order.tableWidget_2.setItem(row, 1, item_name)
            self.dialog_order.tableWidget_2.setItem(row, 2, order_item_amount)
            self.dialog_order.tableWidget_2.setItem(row, 3, item_amount)

            row += 1

    def search_all_order(self):
        items_data = self.user_model.load_order_data()

        print(f"items_data: {items_data}")
        row = 0

        self.dialog_order.tableWidget.setRowCount(len(items_data))
        print(f"len:{len(items_data)}")

        for item in items_data:
            # Create QTableWidgetItems for each value
            order_id = QTableWidgetItem(str(item[0]))
            order_name = QTableWidgetItem(str(item[1]))
            order_item_id = QTableWidgetItem(str(item[2]))
            order_item_amount = QTableWidgetItem(str(item[3]))

            # Set the flags and alignment
            order_id.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            order_name.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            order_item_id.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            order_item_amount.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

            order_id.setTextAlignment(Qt.AlignCenter)
            order_name.setTextAlignment(Qt.AlignCenter)
            order_item_id.setTextAlignment(Qt.AlignCenter)
            order_item_amount.setTextAlignment(Qt.AlignCenter)

            # Set the items in the table
            self.dialog_order.tableWidget.setItem(row, 0, order_id)
            self.dialog_order.tableWidget.setItem(row, 1, order_name)
            self.dialog_order.tableWidget.setItem(row, 2, order_item_id)
            self.dialog_order.tableWidget.setItem(row, 3, order_item_amount)

            row += 1

    def new_item(self):
        new_item_name = self.dialog_operate.lineEdit_new_name.text()
        new_item_firm = self.dialog_operate.lineEdit_new_firm.text()
        new_item_price = self.dialog_operate.lineEdit_new_price.text()
        new_item_amount = self.dialog_operate.lineEdit_new_amount.text()

        if not new_item_name or not new_item_firm or not new_item_price or not new_item_amount:
            QMessageBox.critical(self, '新增品項失敗', '尚有欄位未填寫！')
            return

        if new_item_price.isdigit() != True:
            QMessageBox.critical(self, '新增品項失敗', '單價只能填數字！')
            return

        if new_item_amount.isdigit() != True:
            QMessageBox.critical(self, '新增品項失敗', '數量只能填數字！')
            return

        if self.user_model.search_item_name_and_item_firm(new_item_name, new_item_firm) != False:
            QMessageBox.critical(self, '新增品項失敗', '已有此商品和廠商！')
            return

        self.user_model.new_item(new_item_name, new_item_firm, new_item_price, new_item_amount)
        QMessageBox.information(self, '新增品項成功', '新增品項成功！')

        print(f"new_item_name : {type(new_item_name)} : {new_item_name}")
        print(f"new_item_firm : {type(new_item_firm)} : {new_item_firm}")
        print(f"new_item_price : {type(new_item_price)} : {new_item_price}")
        print(f"new_item_amount : {type(new_item_amount)} : {new_item_amount}")

    def update_item(self):
        update_item_id = self.dialog_operate.lineEdit_update_id.text()
        update_item_name = self.dialog_operate.lineEdit_update_name.text()
        update_item_firm = self.dialog_operate.lineEdit_update_firm.text()
        update_item_price = self.dialog_operate.lineEdit_update_price.text()
        update_item_amount = self.dialog_operate.lineEdit_update_amount.text()

        if not update_item_id or not update_item_name or not update_item_firm or not update_item_price or not update_item_amount:
            QMessageBox.critical(self, '更新品項失敗', '請填寫所有欄位！')
            return

        if self.user_model.search_item_id(update_item_id) != True:
            print(f"沒有此ID")
            QMessageBox.critical(self, '更新品項失敗', '沒有找到此ID！')
            return

        if self.user_model.update_item_check(update_item_id, update_item_name, update_item_firm) != False:
            print(f"重複商品")
            QMessageBox.critical(self, '更新品項失敗', '已重複的商品和廠商！')
            return

        self.user_model.update_item(update_item_id, update_item_name, update_item_firm, update_item_price,
                                    update_item_amount)
        QMessageBox.information(self, '更新品項成功', '更新品項成功！')

    def deltet_id_text(self, event):
        # self.dialog_operate.lineEdit_del_id.clear()
        # self.dialog_operate.lineEdit_del_id.setFocus()
        # self.dialog_operate.lineEdit_del_id.cursor()
        # selected_text = self.dialog_operate.lineEdit_del_id.selectedText()
        # # 在这里执行处理选中文本的操作
        # print("Selected Text:", selected_text)
        self.dialog_operate.lineEdit_del_id.setText(" ")  # 设置一个空格或其他不可见字符
        self.dialog_operate.lineEdit_del_id.clear()  # 清空文本框内容
        pass

    def delete_item(self):
        delete_item_id = self.dialog_operate.lineEdit_del_id.text()
        delete_item_name = self.dialog_operate.lineEdit_del_name.text()
        delete_item_firm = self.dialog_operate.lineEdit_del_firm.text()

        if not delete_item_id and not delete_item_name and not delete_item_firm:
            print(f"刪除品項失敗")
            QMessageBox.critical(self, '刪除品項失敗', '請填寫其中一個欄位！')
            return
        else:
            if self.user_model.search_item_id(delete_item_id) != True and delete_item_id:
                QMessageBox.critical(self, '刪除品項失敗', '沒有找到此ID！')
                return
            if self.user_model.search_item_name(delete_item_name) != True and delete_item_name:
                QMessageBox.critical(self, '刪除品項失敗', '沒有找到此商品！')
                return
            if self.user_model.search_item_firm(delete_item_firm) != True and delete_item_firm:
                QMessageBox.critical(self, '刪除品項失敗', '沒有找到此廠商！')
                return
            self.user_model.delete_item(delete_item_id, delete_item_name, delete_item_firm)
            QMessageBox.information(self, '刪除品項成功', '刪除品項成功！')

    def search_item(self):
        search_item_id = self.dialog_operate.lineEdit_search_id.text()
        search_item_name = self.dialog_operate.lineEdit_search_name.text()
        search_item_firm = self.dialog_operate.lineEdit_search_firm.text()

        if not search_item_id and not search_item_name and not search_item_firm:
            print(f"搜尋品項失敗")
            QMessageBox.critical(self, '搜尋品項失敗', '請填寫其中一個欄位！')
            return
        else:
            if self.user_model.search_item_id(search_item_id) != True and search_item_id:
                QMessageBox.critical(self, '搜尋品項失敗', '沒有找到此ID！')
                return
            if self.user_model.search_item_name(search_item_name) != True and search_item_name:
                QMessageBox.critical(self, '搜尋品項失敗', '沒有找到此商品！')
                return
            if self.user_model.search_item_firm(search_item_firm) != True and search_item_firm:
                QMessageBox.critical(self, '搜尋品項失敗', '沒有找到此廠商！')
                return

            items_data = self.user_model.search_item(search_item_id, search_item_name, search_item_firm)
            print(f"items_data: {items_data}")
            row = 0

            self.dialog_operate.tableWidget.setRowCount(len(items_data))
            print(f"len:{len(items_data)}")

            for item in items_data:
                # Create QTableWidgetItems for each value
                item_id_item = QTableWidgetItem(str(item[0]))
                item_name_item = QTableWidgetItem(str(item[1]))
                item_firm_item = QTableWidgetItem(str(item[2]))
                unit_price_item = QTableWidgetItem(str(item[3]))
                quantity_item = QTableWidgetItem(str(item[4]))

                print(f"item_id_item : {type(item[0])} : {item[0]}")
                print(f"item_name_item : {type(item[1])} : {item[1]}")
                print(f"item_firm_item : {type(item[2])} : {item[2]}")
                print(f"unit_price_item : {type(item[3])} : {item[3]}")
                print(f"quantity_item : {type(item[4])} : {item[4]}")

                # Set the flags and alignment
                item_id_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                item_name_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                item_firm_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                unit_price_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
                quantity_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

                item_id_item.setTextAlignment(Qt.AlignCenter)
                item_name_item.setTextAlignment(Qt.AlignCenter)
                item_firm_item.setTextAlignment(Qt.AlignCenter)
                unit_price_item.setTextAlignment(Qt.AlignCenter)
                quantity_item.setTextAlignment(Qt.AlignCenter)

                # Set the items in the table
                self.dialog_operate.tableWidget.setItem(row, 0, item_id_item)
                self.dialog_operate.tableWidget.setItem(row, 1, item_name_item)
                self.dialog_operate.tableWidget.setItem(row, 2, item_firm_item)
                self.dialog_operate.tableWidget.setItem(row, 3, unit_price_item)
                self.dialog_operate.tableWidget.setItem(row, 4, quantity_item)

                row += 1

            QMessageBox.information(self, '搜尋品項成功', '搜尋品項成功！')
            pass

    def on_login(self):
        account = self.dialog_login.lineEdit_account.text()
        password = self.dialog_login.lineEdit_password.text()

        if not account or not password:
            QMessageBox.critical(self, '登入失敗', '帳號或密碼未填寫！')
            return

        result = self.user_model.check_login(account, password)

        if result:
            QMessageBox.information(self, '登入成功', '登入成功！')
            # 在這裡進入系統畫面，你可以根據需要建立新的視窗或畫面
            self.show_operate_window()
            # self.close()
        else:
            QMessageBox.critical(self, '登入失敗', '帳號或密碼錯誤！')

    def on_register(self):
        new_account = self.dialog_register.lineEdit_new_account.text()
        new_password = self.dialog_register.lineEdit_new_password.text()
        check_password = self.dialog_register.lineEdit_check_password.text()

        if not new_account or not new_password or not check_password:
            QMessageBox.critical(self, '註冊失敗', '請填寫所有欄位！')
            return

        if self.user_model.check_existing_account(new_account):
            QMessageBox.critical(self, '註冊失敗', '該帳號已經存在！')
            return

        if new_password != check_password:
            QMessageBox.critical(self, '註冊失敗', '確認密碼不一致！')
            return

        self.user_model.register_account(new_account, new_password)
        QMessageBox.information(self, '註冊成功', '註冊成功！')
        self.show_login_window()

    def show_login_window(self):
        self.setWindowTitle('倉管系統-登入畫面')
        self.resize(700, 300)
        self.stacked_widget.setCurrentWidget(self.dialog_login)

    def show_register_window(self):
        self.setWindowTitle('倉管系統-註冊畫面')
        self.resize(700, 300)
        self.stacked_widget.setCurrentWidget(self.dialog_register)

    def show_operate_window(self):
        self.setWindowTitle('倉管系統-倉庫畫面')
        self.resize(1000, 450)
        self.dialog_operate.tableWidget.setColumnWidth(0, 100)
        self.dialog_operate.tableWidget.setColumnWidth(1, 100)
        self.dialog_operate.tableWidget.setColumnWidth(2, 100)
        self.dialog_operate.tableWidget.setColumnWidth(3, 100)
        self.dialog_operate.tableWidget.setColumnWidth(4, 100)

        self.load_data()

        # self.dialog_operate.tableWidget.itemSelectionChanged.connect(self.on_item_selected_one)

        # 將 focusInEvent 事件連接到自定義槽函數
        # self.dialog_operate.lineEdit_del_id.focusInEvent = self.deltet_id_text

        # 倉庫
        self.dialog_operate.lineEdit_del_id.installEventFilter(self)
        self.dialog_operate.lineEdit_del_name.installEventFilter(self)
        self.dialog_operate.lineEdit_del_firm.installEventFilter(self)

        self.dialog_operate.lineEdit_search_id.installEventFilter(self)
        self.dialog_operate.lineEdit_search_name.installEventFilter(self)
        self.dialog_operate.lineEdit_search_firm.installEventFilter(self)

        self.dialog_operate.tableWidget.viewport().installEventFilter(self)

        # 訂單
        self.dialog_order.lineEdit_del_order_id.installEventFilter(self)
        self.dialog_order.lineEdit_del_order_name.installEventFilter(self)

        self.dialog_order.lineEdit_search_order_id.installEventFilter(self)
        self.dialog_order.lineEdit_search_order_name.installEventFilter(self)

        self.dialog_order.tableWidget.viewport().installEventFilter(self)

        # INIT完 進入登入畫面
        self.stacked_widget.setCurrentWidget(self.dialog_operate)

    def show_order_window(self):
        self.setWindowTitle('倉管系統-訂單畫面')
        self.resize(1000, 460)
        self.dialog_order.tableWidget.setColumnWidth(0, 100)
        self.dialog_order.tableWidget.setColumnWidth(1, 100)
        self.dialog_order.tableWidget.setColumnWidth(2, 100)
        self.dialog_order.tableWidget.setColumnWidth(3, 100)

        # # 假設列出您要設定的新欄位名稱的列表
        # new_column_names = ["欄位1", "欄位2", "欄位3"]
        #
        # # 設定表格的列數
        # self.dialog_order.tableWidget_2.setColumnCount(len(new_column_names))
        #
        # # 設定表格的水平標題
        # self.dialog_order.tableWidget_2.setHorizontalHeaderLabels(new_column_names)

        # 設定 QTableWidget 的水平項目自動調整大小
        # self.dialog_order.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)

        self.dialog_order.tableWidget_2.setColumnWidth(0, 100)
        self.dialog_order.tableWidget_2.setColumnWidth(1, 100)
        self.dialog_order.tableWidget_2.setColumnWidth(2, 100)
        self.dialog_order.tableWidget_2.setColumnWidth(3, 100)
        # self.dialog_operate.lineEdit_del_id.installEventFilter(self)
        # self.dialog_operate.lineEdit_del_name.installEventFilter(self)
        # self.dialog_operate.lineEdit_del_firm.installEventFilter(self)
        #
        # self.dialog_operate.lineEdit_search_id.installEventFilter(self)
        # self.dialog_operate.lineEdit_search_name.installEventFilter(self)
        # self.dialog_operate.lineEdit_search_firm.installEventFilter(self)
        #
        # self.dialog_operate.tableWidget.viewport().installEventFilter(self)

        self.search_all_order()
        self.search_all_order_item()

        self.stacked_widget.setCurrentWidget(self.dialog_order)

    def eventFilter(self, watched, event):
        # handling focus-in event of the QLineEdit
        if event.type() == event.Type.MouseButtonPress and watched is self.dialog_operate.tableWidget.viewport():
            # item = self.dialog_operate.tableWidget.itemAt(event.position().toPoint())
            # if item is not None:
            #     column_index = item.column()
            #     data = item.text()
            #     print(f"data: {data}")
            item = self.dialog_operate.tableWidget.itemAt(event.position().toPoint())
            if item is not None:
                column_index = item.column()
                if column_index == 0:  # Check if it's the first column
                    row = item.row()
                    row_data = [self.dialog_operate.tableWidget.item(row, col).text() for col in
                                range(self.dialog_operate.tableWidget.columnCount())]
                    print(f"Row Data: {row_data}")
                    self.dialog_operate.lineEdit_update_id.setText(row_data[0])
                    self.dialog_operate.lineEdit_update_name.setText(row_data[1])
                    self.dialog_operate.lineEdit_update_firm.setText(row_data[2])
                    self.dialog_operate.lineEdit_update_price.setText(row_data[3])
                    self.dialog_operate.lineEdit_update_amount.setText(row_data[4])
            return False

        if watched == self.dialog_order.lineEdit_search_order_id and event.type() == event.Type.FocusIn:
            print("Doing something when lineEdit_del_id gets focus.")
            # Clear the content when the lineEdit_del_id gets focus
            # self.dialog_order.lineEdit_del_order_id.clear()
            self.dialog_order.lineEdit_search_order_name.clear()
            # returning True means that the event has been handled, and it should not be further propagated
            return False

        if watched == self.dialog_order.lineEdit_search_order_name and event.type() == event.Type.FocusIn:
            print("Doing something when lineEdit_del_id gets focus.")
            # Clear the content when the lineEdit_del_id gets focus
            self.dialog_order.lineEdit_search_order_id.clear()
            # self.dialog_order.lineEdit_del_order_name.clear()
            # returning True means that the event has been handled, and it should not be further propagated
            return False

        if watched == self.dialog_order.lineEdit_del_order_id and event.type() == event.Type.FocusIn:
            print("Doing something when lineEdit_del_id gets focus.")
            # Clear the content when the lineEdit_del_id gets focus
            # self.dialog_order.lineEdit_del_order_id.clear()
            self.dialog_order.lineEdit_del_order_name.clear()
            # returning True means that the event has been handled, and it should not be further propagated
            return False

        if watched == self.dialog_order.lineEdit_del_order_name and event.type() == event.Type.FocusIn:
            print("Doing something when lineEdit_del_id gets focus.")
            # Clear the content when the lineEdit_del_id gets focus
            self.dialog_order.lineEdit_del_order_id.clear()
            # self.dialog_order.lineEdit_del_order_name.clear()
            # returning True means that the event has been handled, and it should not be further propagated
            return False

        if watched == self.dialog_operate.lineEdit_del_id and event.type() == event.Type.FocusIn:
            print("Doing something when lineEdit_del_id gets focus.")
            # Clear the content when the lineEdit_del_id gets focus
            # self.dialog_operate.lineEdit_del_id.clear()
            self.dialog_operate.lineEdit_del_name.clear()
            self.dialog_operate.lineEdit_del_firm.clear()
            # returning True means that the event has been handled, and it should not be further propagated
            return False

        if watched == self.dialog_operate.lineEdit_del_name and event.type() == event.Type.FocusIn:
            print("Doing something when lineEdit_del_id gets focus.")
            # Clear the content when the lineEdit_del_id gets focus
            self.dialog_operate.lineEdit_del_id.clear()
            # self.dialog_operate.lineEdit_del_name.clear()
            self.dialog_operate.lineEdit_del_firm.clear()
            # returning True means that the event has been handled, and it should not be further propagated
            return False

        if watched == self.dialog_operate.lineEdit_del_firm and event.type() == event.Type.FocusIn:
            print("Doing something when lineEdit_del_id gets focus.")
            # Clear the content when the lineEdit_del_id gets focus
            self.dialog_operate.lineEdit_del_id.clear()
            self.dialog_operate.lineEdit_del_name.clear()
            # self.dialog_operate.lineEdit_del_firm.clear()
            # returning True means that the event has been handled, and it should not be further propagated
            return False

        if watched == self.dialog_operate.lineEdit_search_id and event.type() == event.Type.FocusIn:
            print("Doing something when lineEdit_del_id gets focus.")
            # Clear the content when the lineEdit_del_id gets focus
            # self.dialog_operate.lineEdit_search_id.clear()
            self.dialog_operate.lineEdit_search_name.clear()
            self.dialog_operate.lineEdit_search_firm.clear()
            # returning True means that the event has been handled, and it should not be further propagated
            return False

        if watched == self.dialog_operate.lineEdit_search_name and event.type() == event.Type.FocusIn:
            print("Doing something when lineEdit_del_id gets focus.")
            # Clear the content when the lineEdit_del_id gets focus
            self.dialog_operate.lineEdit_search_id.clear()
            # self.dialog_operate.lineEdit_search_name.clear()
            self.dialog_operate.lineEdit_search_firm.clear()
            # returning True means that the event has been handled, and it should not be further propagated
            return False

        if watched == self.dialog_operate.lineEdit_search_firm and event.type() == event.Type.FocusIn:
            print("Doing something when lineEdit_del_id gets focus.")
            # Clear the content when the lineEdit_del_id gets focus
            self.dialog_operate.lineEdit_search_id.clear()
            self.dialog_operate.lineEdit_search_name.clear()
            # self.dialog_operate.lineEdit_search_firm.clear()
            # returning True means that the event has been handled, and it should not be further propagated
            return False

        # canonical way of handling all other events
        return super().eventFilter(watched, event)

    # def on_item_selected_one(self):
    #     selected_items = self.form2.tableWidget.selectedItems()
    #     if selected_items:
    #         selected_item = selected_items[0]
    #         row = selected_item.row()
    #         column = selected_item.column()
    #         data = selected_item.text()
    #         print(f"Selected Cell: Row={row}, Column={column}, Data={data}")

    def on_item_selected_one(self):
        selected_items = self.dialog_operate.tableWidget.selectedItems()
        if selected_items:
            selected_item = selected_items[0]
            column = selected_item.column()

            if column == 0:  # Only show the information if the first column is selected
                row = selected_item.row()
                data = [self.dialog_operate.tableWidget.item(row, col).text() for col in
                        range(self.dialog_operate.tableWidget.columnCount())]
                print(f"Selected Row Data: {data}")

                update_item_id = data[0]
                update_item_name = data[1]
                update_item_firm = data[2]
                update_item_price = data[3]
                update_item_amount = data[4]

                self.dialog_operate.lineEdit_update_id.setText(update_item_id)
                self.dialog_operate.lineEdit_update_name.setText(update_item_name)
                self.dialog_operate.lineEdit_update_firm.setText(update_item_firm)
                self.dialog_operate.lineEdit_update_price.setText(update_item_price)
                self.dialog_operate.lineEdit_update_amount.setText(update_item_amount)

                # update_item_id = self.dialog_operate.lineEdit_update_id.text()
                # update_item_name = self.dialog_operate.lineEdit_update_name.text()
                # update_item_firm = self.dialog_operate.lineEdit_update_firm.text()
                # update_item_price = self.dialog_operate.lineEdit_update_price.text()
                # update_item_amount = self.dialog_operate.lineEdit_update_amount.text()


            else:
                print(f"沒有選到")

    def on_item_selected_row(self):
        selected_items = self.dialog_operate.tableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            data = [self.dialog_operate.tableWidget.item(selected_row, col).text() for col in
                    range(self.dialog_operate.tableWidget.columnCount())]
            print(f"Selected Row Data: {data}")

    def load_data(self):

        items_data = self.user_model.load_data()
        print(f"items_data: {items_data}")
        row = 0

        self.dialog_operate.tableWidget.setRowCount(len(items_data))
        print(f"len:{len(items_data)}")

        for item in items_data:
            # Create QTableWidgetItems for each value
            item_id_item = QTableWidgetItem(str(item[0]))
            item_name_item = QTableWidgetItem(str(item[1]))
            item_firm_item = QTableWidgetItem(str(item[2]))
            unit_price_item = QTableWidgetItem(str(item[3]))
            quantity_item = QTableWidgetItem(str(item[4]))

            print(f"item_id_item : {type(item[0])} : {item[0]}")
            print(f"item_name_item : {type(item[1])} : {item[1]}")
            print(f"item_firm_item : {type(item[2])} : {item[2]}")
            print(f"unit_price_item : {type(item[3])} : {item[3]}")
            print(f"quantity_item : {type(item[4])} : {item[4]}")

            # Set the flags and alignment
            item_id_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item_name_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            item_firm_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            unit_price_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)
            quantity_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

            item_id_item.setTextAlignment(Qt.AlignCenter)
            item_name_item.setTextAlignment(Qt.AlignCenter)
            item_firm_item.setTextAlignment(Qt.AlignCenter)
            unit_price_item.setTextAlignment(Qt.AlignCenter)
            quantity_item.setTextAlignment(Qt.AlignCenter)

            # Set the items in the table
            self.dialog_operate.tableWidget.setItem(row, 0, item_id_item)
            self.dialog_operate.tableWidget.setItem(row, 1, item_name_item)
            self.dialog_operate.tableWidget.setItem(row, 2, item_firm_item)
            self.dialog_operate.tableWidget.setItem(row, 3, unit_price_item)
            self.dialog_operate.tableWidget.setItem(row, 4, quantity_item)

            row += 1