# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/18 15:59
@Author  : MaSai
@FileName: index_mian_page.py
@SoftWare: PyCharm
"""
from time import sleep

from selenium.webdriver.common.by import By

from Test_python.Test_web.test_page.Add_Number_Page import Add_Number_Page

"""
定位元素相同的元素有多个字节点 classname:nth-child(1) 从1开始
$('.index_service_cnt_itemWrap:nth-child(1)')
(".member_colRight_memberTable_td:nth-child(2)")
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Index_Main_Page():
    def __init__(self):
        # options=Options()
        # options.add_argument="127.0.0.1:9222"
        # self.driver=webdriver.Chrome(options=options)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # self.driver.implicitly_wait(5)

        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def addnumber(self):
        sleep(5)
        # self.driver.find_element_by_css_selector(".index_service_cnt_itemWrap:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap:nth-child(1)").click()
        return Add_Number_Page(self.driver)
