#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Time    : 2021/5/4 12:56
# @Author  : 黄权权
# @File    : homePage.py
# @Software: PyCharm
# @Desc    : 淘宝首页
import allure
import pytest
from pylib.web_UI_lib.pageObjects.commonPage import CommonPage

class HomePage(CommonPage):
    """
    首页
    """

    def __init__(self):
        # 继承父类的__init__()构造方法
        super(HomePage, self).__init__()

        # 1、顶部superbanner模块
        # 2、中部搜索模块，logo，热点搜索，二维码
        # 3、中部导航栏——主题市场模块
        # 4、左侧分类栏
        # 5、中间的轮播图
        # 6、右侧模块
        # 7、中部的bannner
        # 8、有好货模块
        # 9、有好货模块下面的banner
        # 10、猜你喜欢模块
        # 11、最右侧的浮动导航栏



