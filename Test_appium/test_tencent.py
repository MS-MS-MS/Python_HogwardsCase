# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/10 16:18
@Author  : ms
@FileName: test_tencent.py
@SoftWare: PyCharm
"""
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

"""
企业微信
添加联系人
删除联系人
"""
class Test_Wework:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
        desired_caps["noReset"] = 'true'

        desired_caps['skipDeviceInitialization'] = True
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
        pass

    def treadown(self):
        pass

    def test_add(self):

        """
        添加联系人
        :return:
        """
        add_name="001"
        gender='男'
        phone_number='13400000001'

        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("添加成员").'
                                                        'instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()

        self.driver.find_element(MobileBy.XPATH,"//*[@class='android.widget.EditText'and @text='必填']").send_keys(add_name)

        # curry_text=self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        self.driver.find_element(MobileBy.XPATH,"//*[@text='性别']/../*[@class='android.widget.RelativeLayout']").click()

        WebDriverWait(self.driver,10).until(lambda x:self.driver.find_element(MobileBy.XPATH,"//*[@text='女']"))
        if gender=='男':
            self.driver.find_element(MobileBy.XPATH,"//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH,"//*[@text='女']").click()

        self.driver.find_element(MobileBy.XPATH,"//*[@text='手机号']").send_keys(phone_number)

        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("保存").'
     
                                                        'instance(0));').click()
    def test_rem(self):
        """
        删除联系人
        :return:
        """
        self.driver.find_element(MobileBy.XPATH,"//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text ='管理企业']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text ='成员与部门管理']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text ='测试1']").click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().textContains("删除成员").'
                                                        'instance(0));').click()

        self.driver.find_element(MobileBy.XPATH, "//*[@text ='确定']").click()


