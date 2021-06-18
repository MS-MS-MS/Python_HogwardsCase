# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/18 14:52
@Author  : MaSai
@FileName: LoginPage.py
@SoftWare: PyCharm
"""
from selenium.webdriver.remote.webdriver import WebDriver

from Test_python.Test_web.test_page.RegisterPage import Register

"""
登录类
"""
class LoginPage():
    #规定的类型首字母要大写
    def __init__(self,deiver:WebDriver):
        self.driver=deiver

    # 扫码
    def saoma(self):
        pass
    # 立即注册
    def register(self):
        self.driver.find_element_by_xpath('//*[@id="wework_admin.loginpage_wx_$"]/main/div[2]/a').click()
        return Register(self.driver)
