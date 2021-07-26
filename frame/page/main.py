# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/22 17:35
@Author  : MaSai
@FileName: main.py
@SoftWare: PyCharm
"""
from selenium.webdriver.common.by import By

from frame.page.BasePage import BasePage
from frame.page.market import Market

"点击行情按钮"


class Main(BasePage):

    # def __init__(self):
    def goto_market(self):
        """
        点击登录
        :return:
        """
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/post_status']").click()
        # """
        # 点击行情
        # """
        # self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/tab_name'and@text='行情']").click()
        # 传入当前方法对应的ymal文件,方法名
        self.perse_yaml("../datas/main.yaml","goto_market")
        return Market(self.driver)
