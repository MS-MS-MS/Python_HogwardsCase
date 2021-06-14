# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/12 16:28
@Author  : ms
@FileName: test_selenium.py
@SoftWare: PyCharm
"""
import selenium
from selenium import webdriver
import time
import pytest
# def test_selenium():
#     dirver =webdriver.Chrome()
#     dirver.get("https://www.baidu.com/")

#创建一个测试类
class Test_selenium:
    def setup(self):
        #初始化，创建一个webdriver.Chrom()实例
        self.diriver =webdriver.Chrome()
        # 指定获取的URl
        self.diriver.get("https://testerhome.com/")
        # 创建一个隐式等待 查看元素是否存在  全局控制
        self.diriver.implicitly_wait(5)

    def treadown(self):
        # 等待2秒之后资源回收
        time.sleep(2)
        self.diriver.quit()

    # 测试的方法
    def test_hogwards(self):
        # 点击标签
        self.diriver.find_element_by_link_text("社团").click()
        self.diriver.find_element_by_link_text("君海游戏QA").click()
        self.diriver.find_element_by_css_selector(".topic-22758 .title > a").click()
