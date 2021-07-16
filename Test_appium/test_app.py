# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/8 22:00
@Author  : ms
@FileName: test_app.py
@SoftWare: PyCharm
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class Test_wework:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
        desired_caps["noReset"] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
    def treadown(self):
        pass

    def test_local(self):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("打卡").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()

        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        # expected_conditions
        WebDriverWait(self.driver, 10).until(lambda x: "外出打卡成功" in x.page_source)
        # print(self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'Clicked popup')]").text)