#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 9:25
# @File : main.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 测试入口文件
import pytest

if __name__ == '__main__':
    pytest.main(["-s", "-k test_test.py"])
