from view import *
from controller import *
from main import *

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout, \
    QHBoxLayout, QStackedWidget, QMessageBox
from PySide6 import QtWidgets as qtw
# -*- coding: utf-8 -*-
import pymysql


# model.py
class UserModel:
    def __init__(self):
        self.db = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='qwer0147@Q@',
            database='web_test',
            charset="utf8",
        )
        self.cursor = self.db.cursor()

    def commit_changes(self):
        self.db.commit()

    def refresh_data(self):
        self.db.rollback()  # 還原任何未提交的更改，以確保取得最新的資料
        self.load_data()

    def db_connect(self):
        self.db = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='qwer0147@Q@',
            database='web_test',
            charset="utf8",
        )

    def load_data(self):
        # self.db.rollback()  # 還原任何未提交的更改，以確保取得最新的資料
        self.db_connect()
        self.cursor = self.db.cursor()
        query = "SELECT * FROM items"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        # self.db.commit()
        self.db.close()
        return result

    def load_order_data(self):
        # self.db.rollback()  # 還原任何未提交的更改，以確保取得最新的資料
        self.db_connect()
        self.cursor = self.db.cursor()
        query = "SELECT * FROM orders"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        # self.db.commit()
        self.db.close()
        return result

    def load_order_item_data(self):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = "SELECT orders.order_name, items.item_name, orders.order_item_amount, items.item_amount " \
                "FROM orders " \
                "LEFT JOIN items ON orders.order_item_id = items.item_id"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        # self.db.commit()
        self.db.close()
        return result

    def new_order(self, order_name, order_item_id, order_item_amount):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"INSERT INTO orders (order_name, order_item_id, order_item_amount) VALUES ('{order_name}', '{order_item_id}', '{order_item_amount}')"
        self.cursor.execute(query)
        self.db.commit()
        self.db.close()

    def delete_order(self, order_id, order_name):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = ''
        if order_id:
            query = f"DELETE FROM orders WHERE order_id = '{order_id}'"

        if order_name:
            query = f"DELETE FROM orders WHERE order_name = '{order_name}'"

        print(f"delete order query: {query}")
        self.cursor.execute(query)
        self.db.commit()
        self.db.close()
        pass

    def new_item(self, item_name, item_firm, item_price, item_amount):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"INSERT INTO items (item_name, item_firm, item_price, item_amount) VALUES ('{item_name}', '{item_firm}', '{item_price}', '{item_amount}')"
        self.cursor.execute(query)
        self.db.commit()
        self.db.close()

    def search_special_order(self, order_name, order_item_id):
        print(f"search_special_order...")
        self.db_connect()
        self.cursor = self.db.cursor()
        print(f"order_name: {order_name}")
        print(f"order_item_id: {order_item_id}")
        query = ''
        if order_name:
            query = f"SELECT orders.order_name, items.item_name, orders.order_item_amount, items.item_amount " \
                    f"FROM orders " \
                    f"LEFT JOIN items ON orders.order_item_id = items.item_id " \
                    f"WHERE orders.order_name = '{order_name}';"

        if order_item_id:
            query = f"SELECT orders.order_name, items.item_name, orders.order_item_amount, items.item_amount " \
                    f"FROM orders " \
                    f"LEFT JOIN items ON orders.order_item_id = items.item_id " \
                    f"WHERE orders.order_item_id = '{order_item_id}';"

        print(f"query : {query}")
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.db.close()
        print(f"result: {result}")
        return result

    def search_item_name_and_item_firm(self, item_name, item_firm):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"SELECT * FROM items WHERE item_name = '{item_name}' AND item_firm = '{item_firm}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.db.close()
        return result is not None

    def search_order_id(self, order_id):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"SELECT * FROM orders WHERE order_id = '{order_id}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.db.close()
        print(f"result: {result}")
        return result is not None

    def search_order_name(self, order_name):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"SELECT * FROM orders WHERE order_name = '{order_name}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.db.close()
        print(f"result: {result}")
        return result is not None

    def search_order_item_id(self, order_item_id):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"SELECT * FROM orders WHERE order_item_id = '{order_item_id}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.db.close()
        print(f"result: {result}")
        return result is not None

    def search_item_id(self, item_id):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"SELECT * FROM items WHERE item_id = '{item_id}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.db.close()
        print(f"result: {result}")
        return result is not None

    def search_item_name(self, item_name):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"SELECT * FROM items WHERE item_name = '{item_name}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.db.close()
        return result is not None

    def search_item_firm(self, item_firm):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"SELECT * FROM items WHERE item_firm = '{item_firm}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.db.close()
        return result is not None

    def search_item(self, item_id, item_name, item_firm):
        print(f"search item...")
        self.db_connect()
        self.cursor = self.db.cursor()
        print(f"item_id: {item_id}")
        print(f"item_name: {item_name}")
        print(f"item_firm: {item_firm}")
        query = ''
        if item_id:
            query = f"SELECT * FROM items WHERE item_id = '{item_id}'"

        if item_name:
            query = f"SELECT * FROM items WHERE item_name = '{item_name}'"

        if item_firm:
            query = f"SELECT * FROM items WHERE item_firm = '{item_firm}'"

        self.cursor.execute(query)
        result = self.cursor.fetchall()
        self.db.close()
        print(f"result: {result}")
        return result

    def update_item_check(self, item_id, item_name, item_firm):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"SELECT * FROM items WHERE item_id != '{item_id}' AND item_name = '{item_name}' AND item_firm = '{item_firm}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.db.close()
        return result is not None

    def update_item(self, item_id, item_name, item_firm, item_price, item_amount):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"UPDATE items SET item_name = '{item_name}', item_firm = '{item_firm}', item_price = '{item_price}', item_amount = '{item_amount}'WHERE item_id = '{item_id}'"
        self.cursor.execute(query)
        self.db.commit()
        self.db.close()

    def delete_item(self, item_id, item_name, item_firm):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = ''
        if item_id:
            query = f"DELETE FROM items WHERE item_id = '{item_id}'"

        if item_name:
            query = f"DELETE FROM items WHERE item_name = '{item_name}'"

        if item_firm:
            query = f"DELETE FROM items WHERE item_firm = '{item_firm}'"

        print(f"delete query: {query}")
        self.cursor.execute(query)
        self.db.commit()
        self.db.close()
        pass

    def check_login(self, account, password):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"SELECT * FROM users WHERE account = '{account}' AND password = '{password}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.db.close()
        return result is not None

    def check_existing_account(self, account):
        self.db_connect()
        self.cursor = self.db.cursor()
        query = f"SELECT * FROM users WHERE account = '{account}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        self.db.close()
        return result is not None

    def register_account(self, account, password):
        self.db_connect()
        self.cursor = self.db.cursor()
        insert_query = f"INSERT INTO users (account, password) VALUES ('{account}', '{password}')"
        self.cursor.execute(insert_query)
        self.db.commit()
        self.db.close()