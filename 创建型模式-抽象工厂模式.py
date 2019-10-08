# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 13:55
"""
抽象工厂模式

抽象工厂模式是所有形态的工厂模式中最为抽象和最具一般性的一种形态。抽象工厂模式是指当有多个抽象角色时，使用的一种工厂模式。

抽象工厂模式可以向客户端提供一个接口，使客户端在不必指定产品的具体的情况下，创建多个产品族中的产品对象。

根据里氏替换原则，任何接受父类型的地方，都应当能够接受子类型。因此，实际上系统所需要的，仅仅是类型与这些抽象产品角色相同的一些实例，而不是这些抽象产品的实例。

换言之，也就是这些抽象产品的具体子类的实例。工厂类负责创建抽象产品的具体子类的实例。
"""
from monkey_print2 import print


class Xiaomi5:
    def __init__(self):
        self.phone_name = '小米5'

    def send_msg(self):
        print(f'用 {self.phone_name} 发短信')


class Xiaomi6:
    def __init__(self):
        self.phone_name = '小米6'

    def send_msg(self):
        print(f'用 {self.phone_name} 发短信')


class XiaomFactory:
    @staticmethod
    def get_phone(phone_type):
        if phone_type == '5':
            return Xiaomi5()
        elif phone_type == '6':
            return Xiaomi6()


class Apple5:
    def __init__(self):
        self.phone_name = '苹果5'

    def send_msg(self):
        print(f'用 {self.phone_name} 发短信')


class Apple6:
    def __init__(self):
        self.phone_name = '苹果6'

    def send_msg(self):
        print(f'用 {self.phone_name} 发短信')


class AppleFactory:
    @staticmethod
    def get_phone(phone_type):
        if phone_type == '5':
            return Xiaomi5()
        elif phone_type == '6':
            return Xiaomi6()


class FactoryProducer:
    @staticmethod
    def get_factory(factory_name):
        if factory_name == 'xiaomi':
            return XiaomFactory()
        elif factory_name == 'apple':
            return AppleFactory()


if __name__ == '__main__':
    factory = FactoryProducer.get_factory('xiaomi')
    xiaomi5 = factory.get_phone('5')
    xiaomi5.send_msg()

    """
    "D:/coding2/python36patterns/创建型模式-抽象工厂模式.py:22"  14:38:03  用 小米5 发短信
    """
