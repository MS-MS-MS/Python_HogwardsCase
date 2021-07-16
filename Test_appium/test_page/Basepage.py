# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/16 15:55
@Author  : MaSai
@FileName: Basepage.py
@SoftWare: PyCharm
"""

#
#
from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self,driver: WebDriver = None):
        self.driver = driver
