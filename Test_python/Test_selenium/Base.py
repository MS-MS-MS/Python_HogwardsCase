# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/14 10:05
@Author  : ms
@FileName: Base.py
@SoftWare: PyCharm
"""
import os

from selenium import webdriver

"""
基础的类用于创建WebDriver
"""
class Base():
    def setup(self):
        # 多浏览器的处理 按照参数来控制使用浏览器
        # windows的话用set命令设置，并且分行执行
        # 例如：
        # set browser=chrome
        # pytest xxx.py
        browser=os.getenv("browser")
        if browser=="firefox":
            self.driver=webdriver.Firefox()
        elif browser =="headless":
            self.driver =webdriver.PhantomJS()
        else:
            self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()