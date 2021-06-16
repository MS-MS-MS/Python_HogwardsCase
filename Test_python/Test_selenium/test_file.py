# -*- coding: utf-8 -*-
""" 
@Time    : 2021/6/15 15:36
@Author  : MaSai
@FileName: test_file.py
@SoftWare: PyCharm
"""
from time import sleep

from Test_python.Test_selenium.Base import Base

"""
上传文件
"""
class Test_Flie(Base):
    def test_file(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_id("sttb").click()
        self.driver.find_element_by_xpath("//*[@id='uploadImg']").send_keys("D:\Pychon_case\Python_HogwardsCase\Test_python\img\baiduimg.png")
        sleep(10)