# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/16 15:44
@Author  : MaSai
@FileName: MainPage.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from Test_appium.test_page.Basepage import BasePage
from Test_appium.test_page.MailList import MailList

"""
企业微信主页
"""


class MainPage(BasePage):
    # class MainPage:
    #     def __init__(self,driver):
    #         self.driver=driver

    def goto_maillist(self):
        # print("通讯录")
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find(MobileBy.XPATH, "//*[@text='通讯录']").click()
        return MailList(self.driver)
        # return MailList()
