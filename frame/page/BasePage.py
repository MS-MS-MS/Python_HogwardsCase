# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/21 14:21
@Author  : MaSai
@FileName: BasePage.py
@SoftWare: PyCharm
"""
from selenium.webdriver.common.by import By

"""
基类 创建driver
"""
from appium.webdriver.webdriver import WebDriver
from appium import webdriver


class BasePage:
    """
    黑名单
    """
    _blacklist = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            caps = {}
            caps['platformName'] = 'android'
            caps['platformVersion'] = '7.1'
            caps['deviceName'] = '127.0.0.1:21503'
            caps['appPackage'] = 'com.xueqiu.android'
            caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
            caps['noReset'] = "True"
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self.driver.implicitly_wait(5)
        else:
            # self.driver.launch_app()
            self.driver = driver
    """
    定位find方法
    """
    def find(self, by, loactor=None):
        """
        判断传入的位置是否是元祖
        进行黑名单的异常捕获 发现界面的元素和黑名单的元素一致，
        先关闭当前界面,在进行find方法的调用,重新查找该元素
        :param by:
        :param loactor:
        :return:
        """
        try:
            """
            传入元祖进行解包操作
            """
            if loactor == None:
                result = self.driver.find_element(*by)
            else:
                result = self.driver.find_element(by, loactor)
            print(result)
            return result
        # 捕捉黑名单的元素
        except Exception as e:
            for blacl_ele in self._blacklist:
                ele = self.driver.find_elements(*blacl_ele)
                if len(ele) > 0:
                    ele[0].click()
                    # 处理玩黑名单再次查找原来的元素
                    return self.find(by, loactor)

            raise e
