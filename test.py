#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : WaiMaisSystem 
@File    : test.py
@IDE     : PyCharm 
@Author  : 黄权权
@Time    : 2022/8/29 0:47 
@Desc    : 
"""
import os

# # 当前文件的绝对路径
# cur_path = os.path.abspath(__file__)
# print(cur_path)
#
#
# # 获取当前文件所在目录
# cur_dir = os.path.dirname(os.path.abspath(__file__))
# print(cur_dir)
#
# # 获取当前文件所在目录的上一级目录
# cur_dir1 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(cur_dir1)
#
#
# print(os.getcwd())


slink = ["id","myiframe"]
if isinstance(slink,list):
    print("是列表")
else:
    print("不是列表")