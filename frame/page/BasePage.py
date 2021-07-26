# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/21 14:21
@Author  : MaSai
@FileName: BasePage.py
@SoftWare: PyCharm
"""
import yaml
from selenium.webdriver.common.by import By

from frame.page.decorator import Decorator

"""
基类 创建driver
"""
from appium.webdriver.webdriver import WebDriver
from appium import webdriver


class BasePage:
    """
    黑名单
    """
    blacklist = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]

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

    # 加入装饰器 增强find方法，加入黑名单功能
    @Decorator
    def find(self, by, loactor=None):
        if loactor == None:
            result = self.driver.find_element(*by)
        else:
            result = self.driver.find_element(by, loactor)
        return result

    """
    解析yaml 文件
    """

    def perse_yaml(self, path, funcname):
        """
        传入ymal文件的路径, 当前方法名 用于从文件中取数据
        :param path:
        :param funcname:
        :return:
        """
        with open(path, encoding="utf-8") as f:
            data = yaml.safe_load(f)
        #调用perse 传入当前方法的步骤
        self.perse(data[funcname])

    def perse(self, step):
        """
        判断方法的操作，是点击还是输入数据
        :param step:
        :return:
        """
        for steps in step:
            print(steps['action'])
            if 'click' == steps['action']:
                self.find(steps['by'], steps['loactor']).click()
            elif 'send_keys' == steps['action']:
                self.find(steps['by'], steps['loactor']).send_keys(steps['sendkeys'])
