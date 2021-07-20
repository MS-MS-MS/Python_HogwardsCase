# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/16 15:55
@Author  : MaSai
@FileName: Basepage.py
@SoftWare: PyCharm
"""

#
#
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self,by,loaction):
        return self.driver.find_element(by,loaction)

    def finf_slide(self,text):
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                        .scrollable(true).instance(0))\
                                        .scrollIntoView(new UiSelector()\
                                        .text("{text}").instance(0));')
    def get_toast_text(self):
        result = self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        return result

