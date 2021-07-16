# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/16 15:52
@Author  : MaSai
@FileName: ContactAddActivity.py
@SoftWare: PyCharm
"""
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from Test_appium.test_page.Basepage import BasePage


class ContactAddActivity(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    def add(self,add_name,gender,phone_number):
        self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.EditText'and @text='必填']").send_keys(
            add_name)

        # curry_text=self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        self.driver.find_element(MobileBy.XPATH, "//*[@text='性别']/../*[@class='android.widget.RelativeLayout']").click()

        WebDriverWait(self.driver, 10).until(lambda x: self.driver.find_element(MobileBy.XPATH, "//*[@text='女']"))
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text='手机号']").send_keys(phone_number)

        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("保存").'

                                                        'instance(0));').click()
        # print(self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text)
        from Test_appium.test_page.MemberInvite import MemberInvite
        # return MemberInvite(self.driver)
        return MemberInvite(BasePage)
