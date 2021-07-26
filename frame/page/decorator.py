# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/24 9:55
@Author  : ms
@FileName: decorator.py
@SoftWare: PyCharm
"""
import allure


def Decorator(func):
    def  wrapper(*args,**kwargs):
        from frame.page.BasePage import BasePage
        _inance:BasePage=args[0]
        try:
          # 调运find方法
          result=func(*args,**kwargs)
          return result
            # 捕捉黑名单的元素
        except Exception as e:
            # 截图
            _inance.driver.save_screenshot("tmp.png")
            # 以二进制的方式打开图片
            with open("tmp.png","rb") as f:
                content=f.read()
            # 将图片传送给allure
            allure.attach(content,attachment_type=allure.attachment_type.PNG)
            for blacl_ele in _inance.blacklist:
                ele = _inance.driver.find_elements(*blacl_ele)
                if len(ele) > 0:
                    ele[0].click()
                    # 处理玩黑名单再次查找原来的元素
                    return wrapper(*args,**kwargs)

            raise e
    return wrapper