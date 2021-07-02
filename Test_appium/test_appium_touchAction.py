# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/2 14:42
@Author  : MaSai
@FileName: test_appium_touchAction.py
@SoftWare: PyCharm
"""
"""
TouchAction 练习 手势,滑动的练习
press 点击
release 释放
move_to 移动
perfrom 执行
点击(tap)
等待(wait)
长按(longPress)
取消(cancel)
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Test_touch:
    def setup(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        # 跳过设备初始化，包括 i.a. : 安装和运行的设置应用程序或设置的权限
        # desired_caps['skipDeviceInitialization'] = "true"
        self.diviver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.diviver.implicitly_wait(5)
    def treadown(self):
        pass
    def test_action(self):
        action=TouchAction(self.diviver)
        action.press(x=115,y=179).wait(200).move_to(x=361,y=182).wait(200).move_to(x=605,y=179)\
        .wait(200).move_to(x=602,y=415).wait(200).move_to(x=611,y=685).release().perform()
