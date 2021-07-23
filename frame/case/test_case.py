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
        # Main().goto_market()



def enhance(func):
    print("before")
    func()
    print("after")


def tmp(func):
    # a = func
    # def wrapper(参数) = def a (a1)
    def wrapper(*args,**kwargs):
        print("before")
        func(*args,**kwargs)
        print("after")
    return wrapper
@tmp
def a (a1):
    print("a")
    print("a1")
def test_a():
    a(20)