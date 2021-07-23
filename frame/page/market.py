# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/22 17:37
@Author  : MaSai
@FileName: market.py
@SoftWare: PyCharm
"""
from selenium.webdriver.common.by import By

from frame.page.BasePage import BasePage
from frame.page.search import Search

"点击搜素按钮"

class Market(BasePage):
    def goto_search(self):
        self.find(By.XPATH,"//*[@resource-id='com.xueqiu.android:id/action_search']").click()
        return Search(self.driver)