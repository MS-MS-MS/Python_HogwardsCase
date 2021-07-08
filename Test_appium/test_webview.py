# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/5 15:18
@Author  : MaSai
@FileName: test_webview.py
@SoftWare: PyCharm
"""
from appium import webdriver

"""
android webview 练习
"""
class Test_webview:
    def setup(self):
        caps={}
        caps['platformName'] ='android'
        caps['platformVersion'] = '7.1'
        caps['deviceName'] = '127.0.0.1:21503'
        # caps['browserName'] = 'Chrome'
        caps['appPackage']= 'com.android.chrome'
        caps[ 'appActivity']='com.google.android.apps.chrome.Main'
        # 调用工作引擎 安卓已经默认调用了
        caps['automationName']= 'uiautomator2'
        caps["noReset"] = 'true'
        caps["skipDeviceInitialization"] = 'true'
        # 禁用chrome欢迎页
        caps['chromeOptions']={'args': ['--disable-fre']}
        # chromedriverExecutable 指定chromewebdriver 路径
        caps['chromedriverExecutable']='D:\chromewebdriver\chromedriver\chromedriver.exe'
        self.driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub",caps)
        self.driver.implicitly_wait(5)

    def treadown(self):
        pass
    def test_browser(self):
        self.driver.get("http://m.baidu.com")