# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/16 15:04
@Author  : MaSai
@FileName: app.py
@SoftWare: PyCharm
"""
from appium import webdriver

from Test_appium.test_page.Basepage import BasePage
from Test_appium.test_page.MainPage import MainPage
import yaml
"""
用于app的启动重启等操作
"""
with open(r"../datas/data.yml") as f :
        """yaml 文件  a: 1   冒号后面要显示空格"""
        date =yaml.safe_load(f)
        desired_caps = date["desirecaps"]
        ip =date["server"]["ip"]
        port = date["server"]["port"]
        print(desired_caps)

# with open('../datas/data.yml') as f :
#     myconfig = yaml.safe_load(f)
#     desired_caps = myconfig['desirecaps']
#     ip = myconfig['server']['ip']
#     port = myconfig['server']['port']
class app(BasePage):
    def stear(self):
        if self.driver == None:
            # desired_caps = {}
            # desired_caps['platformName'] = 'Android'
            # desired_caps['platformVersion'] = '7.1'
            # desired_caps['deviceName'] = '127.0.0.1:21503'
            # # com.android.settings/com.android.settings.Settings
            # desired_caps['appPackage'] = 'com.tencent.wework'
            # desired_caps['appActivity'] = 'com.tencent.wework.launch.WwMainActivity'
            # desired_caps["noReset"] = 'true'
            #
            # desired_caps['skipDeviceInitialization'] = True
            self.driver = webdriver.Remote(f'http://{ip}:{port}/wd/hub', desired_caps)
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        # self.driver.close()
        # self.driver.launch_app()
        pass

    def quit(self):
        # self.driver.quit()
        pass

    def goto_main(self):
        return MainPage(self.driver)
        # return MainPage()
#
