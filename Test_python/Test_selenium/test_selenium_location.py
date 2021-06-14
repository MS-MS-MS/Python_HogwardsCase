# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/13 9:58
@Author  : ms
@FileName: test_selenium_location.py
@SoftWare: PyCharm
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
web控件定位与常见的操作

//表示选取所以元素
* 表示选取任意元素 
后面接上元素的属性  定位元素的父元素
//从父元素抽取子元素  
//a 父元素存在不存在 a
('//*[@id="s_tab"]//a[last()]')

id, name 是页面中唯一的元素 可以直接进行定位
"""


class Test:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://baidu.com/")

    def test_web(self):
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys("鬼泣")
        self.driver.find_element(By.XPATH,'//*[@id="su"]').click()
