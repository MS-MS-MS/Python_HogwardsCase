# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/16 15:55
@Author  : MaSai
@FileName: test_case.py
@SoftWare: PyCharm
"""
from Test_appium.test_page.app import app


class Test:
    def setup(self):
        self.main = app()
        # self.main=self.app().stear().goto_main()

    def test_case(self):
        add_name = "003"
        gender = '男'
        phone_number = '13400000003'
        result=self.main.stear().goto_main().goto_maillist().Addmembers().goto_ContactAdd().add(add_name, gender,
                                                                                         phone_number).toast()
        assert "添加成功"== result