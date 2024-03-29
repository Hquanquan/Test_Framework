#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : WaiMaisSystem 
@File    : homePage.py
@IDE     : PyCharm 
@Author  : 黄权权
@Time    : 2022/8/28 23:16 
@Desc    : 
"""
from pylib.UIlib.common.basePage import BasePage


class HomePage(BasePage):
    """
    首页


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

    """

    def getHomePage_title(self):
        """
        获取首页的标题
        :return:
        """
        self.click(self.nav_left_Login)
        return self.get_url_title()
