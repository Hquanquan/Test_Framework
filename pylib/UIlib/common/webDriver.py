#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2020/12/4 10:26
# @File : webDriver.py 
# @Author  : 黄权权
# @Software: PyCharm
# @Desc    : 驱动类，负责生成webdriver对象
import configparser

from selenium import webdriver

from logs.logger import Logger
from utils.tools import get_dataTime

logger = Logger(logger="myDriver").getlog()


class Driver:

    # 实现单例模式
    # new方法--通过cls调用，调用new方法后生成对象
    def __new__(cls, *args, **kwargs):
        # 判断该cls是否有对应的实例，hasattr() 函数用于判断对象是否包含对应的属性。如果对象有该属性返回 True，否则返回 False。
        if hasattr(cls, '_instance'):
            return cls._instance
        cls._instance = object.__new__(cls)  # 没有则创建对象
        return cls._instance

    def get_driver(self):
        """
        获取浏览器驱动对象
        只有第一次调用本函数会创建浏览器，然后返回浏览器驱动对象
        第二次及以后都会直接返回浏览器驱动对象，不会重复创建
        """
        # 判断当前对象是否有driver属性，如果有直接返回，如果没有造一个再返回
        if hasattr(self, 'driver'):
            return self.driver

        # dirver 如果没有就读取配置文件进行创建driver
        # 1、读取配置文件的信息，打开相应的浏览器
        # 实例化一个 configparser 对象 config
        config = configparser.ConfigParser()
        # 获取配置文件的路径
        # file_path = "../../../configs/web_config.ini"
        file_path = "configs/web_config.ini"
        # 读取该文件所有内容
        config.read(file_path, encoding="utf-8")
        # 读取浏览器类型信息,并打印日志
        browserName = config.get("browserType", "browserName")
        logger.info("%s You had select %s browser!" % (get_dataTime(), browserName))
        # 读取driver驱动路径信息
        driverPath = config.get("browserType", "driverPath")
        logger.info("%s You had select %s " % (get_dataTime(), driverPath))
        # 读取URl地址信息,并打印日志
        url = config.get("testServer", 'URL')
        logger.info("%s The test server url is %s" % (get_dataTime(), url))

        # 2、根据配置文件打开对应的浏览器和网站
        if browserName == "Chrome":
            self.driver = webdriver.Chrome(driverPath)
            logger.info('%s Starting Chorme browser!' % get_dataTime())
        elif browserName == "Firefox":
            # firefox火狐浏览器的驱动已安装在浏览器上，直接调用即可
            self.driver = webdriver.Firefox()
            logger.info('%s Starting Firefox browser!' % get_dataTime())
        elif browserName == "IE":
            self.driver = webdriver.Ie(driverPath)
            logger.info('%s Starting IE browser!' % get_dataTime())
        else:
            print("未配置此浏览器驱动")
            logger.info("%s 未配置此浏览器驱动:%s" % (get_dataTime(), browserName))
            return
        # 利用获取到的driver 打开浏览器，访问url地址,使用try 语句
        try:
            # 窗口最大化
            self.driver.maximize_window()
            self.driver.get(url)
            logger.info("%s Open url %s " % (get_dataTime(), url))
            # 隐式等待10秒
            self.driver.implicitly_wait(10)
            logger.info("%s Set implicitly wait 10" % get_dataTime())

            # 这里可以登录，进入系统首页再返回driver对象
            # cls.__login()

            # 返回driver实例化对象
            return self.driver
        except Exception as e:
            print(e)
            logger.info(f'{get_dataTime()} {e}')


if __name__ == '__main__':
    driver = Driver().get_driver()
