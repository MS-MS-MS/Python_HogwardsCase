# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/18 16:26
@Author  : MaSai
@FileName: Add_Number_Page.py
@SoftWare: PyCharm
"""
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Test_python.Test_web.test_page.Basepage import BasePage


class Add_Number_Page(BasePage):
    # def __init__(self,driver:WebDriver):
    #     self.driver=driver


    def add(self):
        username="aa"
        memberAdd_acctid="00"
        memberAdd_phone="13000000001"
        sleep(5)
        self.find(By.ID,"username").send_keys(username)
        self.find(By.ID,"memberAdd_acctid").send_keys(memberAdd_acctid)
        self.find(By.ID,"memberAdd_phone").send_keys(memberAdd_phone)
        # self.driver.find_element_by_id()
        # self.driver.find_element_by_xpath('//*[@id="js_contacts77"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        self.find(By.CSS_SELECTOR,".js_btn_save").click()