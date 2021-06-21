# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/21 11:07
@Author  : MaSai
@FileName: Basepage.py
@SoftWare: PyCharm
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

# 基础类 用于创建weddriver 和find方法
class  BasePage:
    # driver:WebDriver

    def __init__(self,driver:WebDriver=None):
        # 复用driver在初始话
        if driver==None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(5)
        else:
            self.driver=driver

    def find(self,by,localtion):
       return self.driver.find_element(by,localtion)