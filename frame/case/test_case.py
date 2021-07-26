# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/21 14:44
@Author  : MaSai
@FileName: test_case.py
@SoftWare: PyCharm
"""
from frame.page.main import Main


class Test_case:
    def test_1(self):
        Main().goto_market().goto_search().search_sendkeys()
        # Main().goto_market().goto_search()


#
# def enhance(func
#     print("before")
#     func()
#     print("after")
#
#
#
# def tmp(func):
#     # a = func
#     # def wrapper(参数) = def a (a1)
#     def wrapper(*args,**kwargs):
#         print("before")
#         func(*args,**kwargs)
#         print("after")
#     return wrapper
# @tmp
# def a (a1):
#     print("a")
#     print("a1")
# def test_a():
#     a(20)

# step = [{'action': 'click', 'by': 'XPATH', 'loactor': '//*[@resource-id="com.xueqiu.android:id/action_search"]'}, {'action': 'click', 'by': 'XPATH', 'loactor': '//*[@resource-id="com.xueqiu.android:id/tab_name"and@text="行情"]'}]
#
# def test_1():
#     for steps in step:
#         print(steps['action'])
#         if 'click' ==steps['action']:
#             print("111")

