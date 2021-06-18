# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/18 14:32
@Author  : MaSai
@FileName: index_page.py
@SoftWare: PyCharm
"""
from selenium import webdriver

from Test_python.Test_web.test_page.LoginPage import LoginPage
from Test_python.Test_web.test_page.RegisterPage import Register

"""
企业微信首页
"""


class MainPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/")

    # 登陆的方式
    def goto_loginpage(self):
        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return LoginPage(self.driver)

    # 立即注册方法
    def goto_register(self):
        self.driver.find_element_by_xpath('//*[@id="tmp"]/div[1]/a').click()
        return Register(self.driver)
