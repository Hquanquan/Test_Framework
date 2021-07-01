#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/7/1 21:21
# @Author  : 黄权权
# @File    : test_test.py
# @Software: PyCharm
# @Desc    :
from pylib.UIlib.pageObjects.homePage import HomePage


class TestTest:

    def test_test(self):
        homePage = HomePage()
        title = homePage.getHomePage_title()
        print(title)
