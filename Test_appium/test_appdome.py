# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/1 15:55
@Author  : MaSai
@FileName: test_appdome.py
@SoftWare: PyCharm
"""
# from appium import webdriver
# desired_caps={}
# desired_caps['platformName']='Android'
# desired_caps['platformVersion']='5.1'
# # desired_caps['deviceName']='emulator-5554'
# desired_caps['deviceName']='127.0.0.1:62001'
# desired_caps['appPackage']='com.xueqiu.android'
# desired_caps['appActivity']='.view.WelcomeActivityAlias'
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


from appium import webdriver
# desired_caps={}
# desired_caps['platformName']='Android'
# desired_caps['platformVersion']='6.0'
# desired_caps['deviceName']='127.0.0.1:7555'
# # com.android.settings/com.android.settings.Settings
# desired_caps['appPackage']='com.android.settings'
# desired_caps['appActivity']='com.android.settings.Settings'
#
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# print("启动【设置】应用")
# driver.quit()




# from appium import webdriver
# desired_caps={}
# desired_caps['platformName']='Android'
# desired_caps['platformVersion']='6.0'
# # desired_caps['deviceName']='emulator-5554'
# desired_caps['deviceName']='127.0.0.1:7555'
# desired_caps['appPackage']='com.xueqiu.android'
# desired_caps['appActivity']='.view.WelcomeActivityAlias'
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

# from appium import webdriver
# desired_caps={}
# desired_caps['platformName']='Android'
# desired_caps['platformVersion']='6.0'
# desired_caps['deviceName']='127.0.0.1:7555'
# desired_caps['appPackage']='com.android.settings'
# desired_caps['appActivity']='com.android.settings.Settings'
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion']='7.1'
desired_caps['deviceName']='127.0.0.1:21503'
# com.android.settings/com.android.settings.Settings
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
desired_caps["noReset"] = 'true'
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
print("启动【设置】应用")
