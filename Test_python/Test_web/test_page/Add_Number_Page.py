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


class Add_Number_Page():
    def __init__(self,driver:WebDriver):
        self.driver=driver


    def add(self):
        username="a"
        memberAdd_acctid="0"
        memberAdd_phone="13000000000"
        sleep(5)
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(memberAdd_acctid)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(memberAdd_phone)
        # self.driver.find_element_by_id()
        # self.driver.find_element_by_xpath('//*[@id="js_contacts77"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        self.driver.find_element(By.CSS_SELECTOR,".js_btn_save").click()