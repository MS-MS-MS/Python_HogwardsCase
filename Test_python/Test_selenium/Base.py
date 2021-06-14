# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/14 10:05
@Author  : ms
@FileName: Base.py
@SoftWare: PyCharm
"""
from selenium import webdriver

"""
基础的类用于创建WebDriver
"""
class Base():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()