# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/30 22:25
@Author  : ms
@FileName: test_app_find.py
@SoftWare: PyCharm
"""
from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_app:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '7.1'
        desired_caps['deviceName'] = '127.0.0.1:21503'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps["noReset"] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
    def treadown(self):
        pass

    def test_find(self):
        """
        打开雪球的首页
        定位首页的搜索框
        判断搜索框是否可用并查看搜索框的name 属性
        打印这个元素的左上角的坐标和他的宽高
        向搜索框输入alibaba
        判断阿里巴巴是否可见
        如果可见打印搜索成功，不可见 打印搜索失败
        """
        element=self.driver.find_element_by_id('com.xueqiu.android:id/home_search')
        search_element=element.is_enabled()
        print(element.text)
        print(element.location)
        print(element.size)
        # print(search_element)
        if search_element==True:
            self.driver.find_element_by_id('com.xueqiu.android:id/home_search').click()
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
            #element_text=self.driver.find_element_by_xpath("//*[resource-id='@com.xueqiu.android:id/name' and @text='阿里巴巴']")
            alibaba_element=self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']")
            element_display= alibaba_element.get_attribute("displayed")
            if element_display=='true':
                print("搜索成功")
            else:
                print("搜索失败")
        else:
            print("over")


    def test_serch(self):
        """
        点击搜索栏 输入阿里巴巴,点击阿里巴巴判断股票的是否大于200
       :return:
        """
        print("搜索")
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')

        # self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']").click()

        # 先定位元素的位置
        # 在调用WebDriverWait 传入driver 和timeout
        # 在.unit()调用expected_condition.element_to_xxxx
        # 识别元素是否可点击，可看见，可用等
        # 若元素已被找到，在定位元素，将定位位置元素以解包的方式传入
        locator=(MobileBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
        currey=float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        assert currey >200

    def test_touchaction(self):
        # 引入TouchAction类,传入driver
        action=TouchAction(self.driver)
        # 获得当前页面的宽和高
        window_rect=self.driver.get_window_rect()
        width=window_rect['width']
        height=window_rect['height']
        x1 =int(width/2)
        y_start=int(height * 4/5)
        y_end=int(height * 1/5)
        """
        press 点击
        release 释放
        move_to 移动
        perfrom 执行
        """
        action.press(x=x1,y=y_start).wait(200).move_to(x=x1,y=y_end).release().perform()
        # action.press(x=240,y=1280).wait(2000).move_to(x=240,y=484).release().perform()


    """
    xpath 定位方式 
    父元素定位子元素 
    
    """
    def test_xpath(self):
        # 先定位股票的价格
        self.driver.find_element_by_id("com.xueqiu.android:id/home_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        # self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name'and @text='阿里巴巴']").click()
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/code'and @text='BABA']").click()
        # 从父元素定位 先定位父元素的位置  在定位子元素位置  /元素[1]
        shares_text=self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/title_container']/android.widget.TextView[2]").text
        print(shares_text)
        # 在由股票的代码定位股票的价格
        # 子元素定位父元素  先定位子元素
        # /.. 子元素的上一层级
        # 在从父元素在定位到子元素
        curry_text=self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']").text
        print(f"当前股票的价格{curry_text}")

    # uiautomator 定位方式
    def test_uiaotomator(self):
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        # 混合元素定位先定位id 在定位文字  处理文字在页存在多个的情况
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/tab_name").text("我的")').click()
        # textContains 查找是否包含账号密码的元素
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys("12344444")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys("1234")
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()

        #定位子节点用法 .childSelector
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/title_container").childSelector(text("股票")').click()
        # 定位兄弟节点、同一级的节点 fromParent
        self.driver.find_element_by_android_uiautomator()


    # 滚动查找元素
    def test_scrllor(self):
        self.driver.find_element_by_android_uiautomator(
            'new UiSelector().resourceId("com.xueqiu.android:id/title_text").text("关注")').click()
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().'
                                                        'scrollable(true).instance(0)).'
                                                        'scrollIntoView(new UiSelector().text("雪盈证券").'
                                                        'instance(0));').click()
        sleep(5)



