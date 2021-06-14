# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/12 18:27
@Author  : ms
@FileName: test_wait.py
@SoftWare: PyCharm
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait

"""
直接等待,隐式等待,显示等待的用例
"""
# 直接等待
class TestWait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")

    def test_wait(self):
        self.driver.find_element(By.XPATH,'//*[@title="在最近的一年，一月，一周或一天最活跃的话题"]').click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,'//*[@title="原创精华文章,有100元奖金"]').click()
# 隐式等待
class TestWait_1:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")
        self.driver.implicitly_wait(3)

    def test_wait_1(self):
        self.driver.find_element(By.XPATH,'//*[@title="在最近的一年，一月，一周或一天最活跃的话题"]').click()
        self.driver.find_element(By.XPATH, '//*[@title="原创精华文章,有100元奖金"]').click()

class TestWait_2:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")

    def test_wait_2(self):
        self.driver.find_element(By.XPATH,'//*[@title="在最近的一年，一月，一周或一天最活跃的话题"]').click()
        def wait(x):
            return len(self.driver.find_element(By.XPATH,'//*[class="table-heading"]')) >=1
        WebDriverWait(self.driver,10).until(wait)
        self.driver.find_element(By.XPATH, '//*[@title="原创精华文章,有100元奖金"]').click()