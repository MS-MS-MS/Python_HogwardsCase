# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/14 11:39
@Author  : ms
@FileName: test_frame.py
@SoftWare: PyCharm
"""
"""
frame 

先切换到字节的在切换回去

"""


from Test_python.Test_selenium.Base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 要定位frame 下的元素，要先切换到frame的子节点
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_xpath('//*[@id="draggable"]').text)
        #切换到父节点
        self.driver.switch_to.parent_frame()
        #切换到初始打开的节点
        # self.driver.switch_to.default_content()
        print(self.driver.find_element_by_xpath('//*[@id="submitBTN"]').text)