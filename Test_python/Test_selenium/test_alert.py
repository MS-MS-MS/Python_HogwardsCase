# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/15 16:00
@Author  : MaSai
@FileName: test_alert.py
@SoftWare: PyCharm
"""
from time import sleep

from selenium.webdriver import ActionChains

from Test_python.Test_selenium.Base import Base


class TestAlert(Base):
    def testalert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换到子节点 出入父节点的id
        self.driver.switch_to_frame("iframeResult")
        drag=self.driver.find_element_by_id("draggable")
        drop=self.driver.find_element_by_id("droppable")
        action=ActionChains(self.driver)
        # 拖拽的命令
        action.drag_and_drop(drag,drop)
        action.perform()
        sleep(5)
        # alert 标签
        print("点击alert 确认")
        # 切换到alert 弹框点击确认按钮
        self.driver.switch_to.alert.accept()
        # self.driver.switch_to_default_content()
        # 切换到frame父节点
        self.driver.switch_to.parent_frame()
        self.driver.find_element_by_id("submitBTN").click()
        sleep(5)