# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/15 10:37
@Author  : MaSai
@FileName: test_selenium_js.py
@SoftWare: PyCharm
"""
"""
调用js的方式定位元素
"""

from time import sleep
import pytest
from selenium.webdriver.common.by import By
from Test_python.Test_selenium.Base import Base


class TestJs(Base):
    @pytest.mark.skip()
    def test_js(self):
        self.driver.get("https://baidu.com/")
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("selenium测试")
        # js的方式定位元素 根据id
        element = self.driver.execute_script('return  document.getElementById("su")')
        element.click()
        # js方式进行滑动操作
        self.driver.execute_script('document.documentElement.scrollTop ="10000"')
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        sleep(5)

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        self.driver.execute_script("a=document.getElementById('train_date').value='2021-6-30'")
        sleep(10)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
