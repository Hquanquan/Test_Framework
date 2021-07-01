#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/3 17:24
# @File : convertData.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import datetime

from utils.tools import read_yaml


class ConvertData:

    @staticmethod
    def current_time(time_formate="%Y-%m-%dT%H:%M:%S.%f", tager=True):
        """
        获取当前时间，转换为指定的字符串格式返回
        :param time_formate: 格式
        :param tager: 默认
        :return:
        """
        dt = datetime.datetime.now()
        current_time = dt.strftime(time_formate)
        if not tager:
            return current_time
        return current_time[:-3] + "Z"

    @staticmethod
    def get_param(path='data/contracts_data.yaml'):
        """
        读取指定配置文件的数据，以列表嵌套列表的形式返回：[[],[],[]]
        :param path:
        :return:
        """
        data = read_yaml(path)
        values = [data[key] for key in data]
        res = []
        for i in range(len(values[0])):
            ele = []
            for k in range(len(values)):
                ele.append(values[k][i])
            res.append(ele)
        return res


if __name__ == '__main__':
    param = ConvertData.get_param()
    print(param)
