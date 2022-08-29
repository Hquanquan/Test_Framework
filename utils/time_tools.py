#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project : WaiMaisSystem 
@File    : time_tools.py
@IDE     : PyCharm 
@Author  : 黄权权
@Time    : 2022/8/29 22:58 
@Desc    : 
"""
import datetime


def get_dataTime(time_formate="%Y-%m-%d %H:%M:%S-%f"):
    """
    获取当前时间，转换为指定的字符串格式返回
    :param time_formate: 格式
    :return:
    """
    dt = datetime.datetime.now()
    current_time = dt.strftime(time_formate)
    return current_time


if __name__ == '__main__':
    print(get_dataTime())

