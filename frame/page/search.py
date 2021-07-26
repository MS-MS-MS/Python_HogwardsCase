# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/22 17:39
@Author  : MaSai
@FileName: search.py
@SoftWare: PyCharm
"""
from selenium.webdriver.common.by import By

from frame.page.BasePage import BasePage


class Search(BasePage):
    def search_sendkeys(self):
        # print("1")
        # self.find(By.XPATH,'//*[@resource-id="com.xueqiu.android: id / search_input_text"]')
        # 传入当前方法对应的ymal文件,方法名
        self.perse_yaml("../datas/search.yaml","search_sendkeys")