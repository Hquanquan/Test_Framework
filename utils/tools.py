#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/2 11:23
# @File : tools.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 通用工具
import datetime
import random
from functools import wraps

import allure
import yaml


def write_yaml(args, path="configs/createCustomers.yaml"):
    """
    写入数据到指定的yaml文件中
    :param args:
    :param path: path="configs/createCustomers.yaml"默认值
    :return:
    """
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(args, f, allow_unicode=True)


def read_yaml(filePath):
    """
    读取yaml文件数据，并字典格式返回
    :param filePath:
    :return:
    """
    # 打开filePath路径的文件
    with open(filePath, encoding="utf-8") as f:
        # 读取yaml文件内容，赋值到content
        content = f.read()
        # 把content转化为字典格式
        data_json = yaml.safe_load(content)
        return data_json


def get_dataTime(time_formate="%Y-%m-%d %H:%M:%S-%f"):
    """
    获取当前时间，转换为指定的字符串格式返回
    :param time_formate: 格式
    :return:
    """
    dt = datetime.datetime.now()
    current_time = dt.strftime(time_formate)
    return current_time


# 自定义的装饰器
def dynamic_report(target, target_tile=None):
    def decorate(fun):
        @wraps(fun)  # 保留测试方法原来的信息
        def warpper(*args, **kwargs):
            res = fun(*args, **kwargs)
            desc = kwargs[target]  # 从用例参数列表获取要表示的字段
            allure.dynamic.description('用例描述---%s' % desc)
            if target_tile:  # 如果指定了目标标题就从参数列表的数据自定义报告标题
                title = kwargs[target_tile]
                allure.dynamic.title(title)
            return res

        return warpper

    return decorate


def get_phone_num():
    """
    生成一个随机的手机号码
    要获取一个手机号，我们首先需要了解手机号码的组成规律，我们简单的认为存在以下规律：
    ①手机号码一共有11位
    ②第1位目前都是1
    ③第2位in[3、4、5、7、8] 取值
    ④第3位比较复杂一些，根据第2位的数字，对应运营商的生成规律
    ⑤后8位是随机生成的8个数字
    :return:
    """
    second_spot = random.choice([3, 4, 5, 7, 8])
    third_spot = {
        3: random.randint(0, 9),
        4: random.choice([5, 7, 9]),
        5: random.choice([i for i in range(10) if i != 4]),
        7: random.choice([i for i in range(10) if i not in [4, 9]]),
        8: random.randint(0, 9), }[second_spot]

    remain_spot = random.randint(9999999, 100000000)
    phone_num = "1{}{}{}".format(second_spot, third_spot, remain_spot)
    return phone_num


def create_Str(text):
    """
    生成以text开头，以当前时间结尾的字符串
    :param text:
    :return:
    """
    return text + get_dataTime(time_formate="%Y%m%d%H%M%S")


if __name__ == '__main__':
    # data = read_yaml(r"../configs/api_conf.yaml")
    # print(get_phone_num())
    # print(create_Str("公司名称"))
    print(get_dataTime(time_formate="%Y-%m"))
