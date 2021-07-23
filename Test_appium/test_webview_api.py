# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/6 10:53
@Author  : MaSai
@FileName: test_webview_api.py
@SoftWare: PyCharm
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_webview:
    def setup(self):
        caps={}
        caps['platformName'] ='android'
        caps['platformVersion'] = '7.1'
        caps['deviceName'] = '127.0.0.1:21503'
        caps['appPackage'] = 'io.appium.android.apis'
        caps['appActivity'] = 'io.appium.android.apis.ApiDemos'
        # 调用工作引擎 安卓已经默认调用了
        caps['automationName']= 'uiautomator2'
        caps['chromedriverExecutable']='D:\chromewebdriver\chromedriver_win32_70.0.3538.16\chromedriver.exe'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)
    def treadown(self):
        # self.driver.quit()
        pass

    def test_webview_api(self):
        print(self.driver.contexts)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='Views']").click()
        views="WebView"
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        f'scrollIntoView(new UiSelector().text("{views}").'
                                                        'instance(0));').click()
        # wbeview_contexts=self.driver.contexts
        # 切换上下文 ，从原生界面切换到webcview页面
        self.driver.switch_to.context(self.driver.contexts[-1])
        self.driver.find_element(MobileBy.ID,'i_am_a_textbox').send_keys("MobileBY")
        self.driver.find_element(MobileBy.ID,'i am a link').click()
        print(self.driver.page_source)
        pass