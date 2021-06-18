# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/18 15:12
@Author  : MaSai
@FileName: test_wx.py
@SoftWare: PyCharm
"""
from Test_python.Test_web.test_page.index_page import MainPage


class TestWx():
    def setup(self):
        self.main=MainPage()

    def test_login(self):
        self.main.goto_loginpage().register().register_send()

    def test_register(self):
        assert True==self.main.goto_register().register_send()
