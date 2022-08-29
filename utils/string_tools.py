#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/4/10 14:07
# @File : string_tools.py
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : None
import hashlib
import random


def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)


def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x} {body:x}'
    str = bytes.fromhex(val).decode('gb2312')
    return str


def get_phone_num():
    """
    生成一个随机的手机号码
    要获取一个手机号，我们首先需要了解手机号码的组成规律，我们简单的认为存在以下规律：
    ①手机号码一共有11位
    ②第1位目前都是1
    ③第2位in[3、4、5、7、8] 取值
    ④第3位比较复杂一些，根据第2位的数字，对应运营商的生成规律
    ⑤后8位是随机生成的8个数字
    :return: 返回值类型是字符串
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


def get_md5(psw):
    """
    MD5加密字符
    :param psw: 需要加密的字符串
    :return: 返回加密后的数据
    """
    # 实例化一个md5对象
    md5 = hashlib.md5()
    # 加密字符
    md5.update(psw.encode('utf-8'))
    # 调用hexdigest()获取加密结果数据，并返回
    return md5.hexdigest()


if __name__ == '__main__':
    print(Unicode())
    print(GBK2312())
    print(type(get_phone_num()))
