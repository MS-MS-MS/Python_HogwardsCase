# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/3 10:53
@Author  : ms
@FileName: test_appium_toast.py
@SoftWare: PyCharm
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

"""
toast 控件练习
文字提示
"""
class Test_toast:
    def setup(self):
        caps={}
        caps['platformName'] ='android'
        caps['platformVersion'] = '7.1'
        caps['deviceName'] = '127.0.0.1:21503'
        caps['appPackage'] = 'io.appium.android.apis'
        caps['appActivity'] = 'io.appium.android.apis.view.PopupMenu1'
        # 调用工作引擎 安卓已经默认调用了
        caps['automationName']= 'uiautomator2'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)
    def treadown(self):
        pass
    def test_toast_case(self):
        self.driver.find_element(MobileBy.ACCESSIBILITY_ID,'Make a Popup!').click()
        self.driver.find_element_by_xpath("//*[@text='Search1']").click()
        # 打印页面元素
        # print(self.driver.page_source)
        # 定位文字提示框 1 xpath 2. contains(@text='')
        # print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup')]").text)