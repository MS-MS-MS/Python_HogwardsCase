# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/6 22:08
@Author  : ms
@FileName: test_webview_genymotion.py
@SoftWare: PyCharm
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
webview 练习 
genymotiom android 6.0

当前找不到元素
"""

class Test_webview:
    def setup(self):
        caps={}
        caps['platformName'] ='android'
        caps['platformVersion'] = '6.0'
        caps['deviceName'] = '192.168.248.101:5555'
        # 调用工作引擎 安卓已经默认调用了
        caps['automationName']= 'uiautomator2'
        # caps["noReset"] = 'true'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # caps["skipDeviceInitialization"] = 'true'
        # chromedriverExecutable 指定chromewebdriver 路径
        # caps['chromedriverExecutable']='D:\chromewebdriver\chromedriver_win32_2.22\chromedriver.exe'
        caps['chromedriverExecutable']='D:\chromewebdriver\chromedriver_win32_74.0.3729.6\chromedriver.exe'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)

    def treadown(self):
        pass

    def test_webview(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='交易']").click()
        A_locator=(MobileBy.XPATH,"//*[@id='Layout_app_3V4']/div/div/ul/li[1]/div[2]/div/span")
        print(self.driver.contexts)
        # 切换上下文
        self.driver.switch_to.context(self.driver.contexts[-1])
        # 点击A股开户
        print(self.driver.window_handles)
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(A_locator))
        self.driver.find_element(*A_locator).click()
        kaihu_window=self.driver.window_handles[-1]
        self.driver.switch_to.window(kaihu_window)

        # print(self.driver.page_source)
        phone_locator =(MobileBy.ID,'phone-number')
        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(phone_locator))
        self.driver.find_element(*phone_locator).send_keys("11111111")