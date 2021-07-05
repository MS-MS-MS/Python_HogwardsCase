# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/3 15:00
@Author  : ms
@FileName: test_appium_yaml.py
@SoftWare: PyCharm
"""
import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from hamcrest import *


def get_yaml():
    with open(r"YAML.yaml")as f:
        date = yaml.safe_load(f)
        # print(date)
        xq = date['date']['code']
        ids = date['date']['ids']
        return [xq, ids]

class Test_app_yaml:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps["noReset"] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
        pass
    def treadown(self):
        self.driver.find_element_by_id('com.xueqiu.android:id/action_close').click()
        pass

    @pytest.mark.parametrize('name,code,price',get_yaml()[0])
    def test_yaml(self,name,code,price):
        # 打开雪球
        # 在搜索框输入股票的名字
        # 点击搜索的股票
        # 通过股票的编号判断估计是否符合预期结果
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys(name)
        self.driver.find_element_by_xpath(f"//*[@resource-id='com.xueqiu.android:id/code'and @text='{code}']").click()
        curry_text =float(self.driver.find_element_by_xpath(
            f"//*[@text='{code}']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text)
        print(curry_text)
        print(price)
        price_closeto =price*0.1
        print(price_closeto)
        assert_that(curry_text,close_to(price,price*0.1))






