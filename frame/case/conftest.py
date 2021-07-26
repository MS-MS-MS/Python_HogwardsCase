# -*- coding: utf-8 -*-
""" 
@Time    : 2021/7/24 18:07
@Author  : ms
@FileName: conftest.py
@SoftWare: PyCharm
"""
import os
import signal
import subprocess

import pytest


@pytest.fixture(scope="module", autouse=True)
def rccord_vedio():
    # 命令
    command = "scrcpy --record tmp.mp4"
    # 使用python subprocess库模拟输入命令
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    yield
    # 结束录屏
    os.kill(p.pid, signal.CTRL_C_EVENT)
