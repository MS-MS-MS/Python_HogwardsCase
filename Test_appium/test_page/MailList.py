# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/16 15:45
@Author  : MaSai
@FileName: MailList.py
@SoftWare: PyCharm
"""
from Test_appium.test_page.Basepage import BasePage
from Test_appium.test_page.MemberInvite import MemberInvite

"""
通讯录
"""


class MailList(BasePage):
    # class MailList:
    #     def __init__(self,driver):
    #         self.driver=driver
    def Addmembers(self):
        # self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
        #                                                 'scrollable(true).instance(0)).'
        #                                                 'scrollIntoView(new UiSelector().textContains("添加成员").'
        #                                                 'instance(0));').click()
        self.finf_slide("添加成员").click()
        return MemberInvite(self.driver)
        # return MemberInvite()
