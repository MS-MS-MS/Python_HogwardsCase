# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/16 15:51
@Author  : MaSai
@FileName: MemberInvite.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy

from Test_appium.test_page.Basepage import BasePage
from Test_appium.test_page.ContactAddActivity import ContactAddActivity

"""
添加成员
"""


class MemberInvite(BasePage):
    # class MemberInvite:
    #     def __init__(self,driver):
    #         self.driver=driver
    def goto_ContactAdd(self):
        self.find(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        return ContactAddActivity(self.driver)
        # return ContactAddActivity()

    def toast(self):
        result= self.get_toast_text()
        # result = self.find(MobileBy.XPATH, "//*[contains(@text,'添加成功')]").text
        return result
