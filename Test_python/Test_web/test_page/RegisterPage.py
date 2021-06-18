# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/18 15:02
@Author  : MaSai
@FileName: RegisterPage.py
@SoftWare: PyCharm
"""
from time import sleep

from selenium.webdriver.remote.webdriver import WebDriver

"""
注册类
"""


class Register():
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    # 输入注册信息
    def register_send(self):
        # sleep(5)
        self.driver.find_element_by_id("corp_name").send_keys("mas")
        self.driver.find_element_by_id('manager_name').send_keys("mass")
        self.driver.find_element_by_id('register_tel').send_keys("13400000000")
        assert True
