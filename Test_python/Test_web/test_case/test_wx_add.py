# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/18 16:37
@Author  : MaSai
@FileName: test_wx_add.py
@SoftWare: PyCharm
"""
from Test_python.Test_web.test_page.index_mian_page import Index_Main_Page


class Test_add():
    def setup(self):
        self.index = Index_Main_Page()

    def test_add(self):
        self.index.addnumber().add()
