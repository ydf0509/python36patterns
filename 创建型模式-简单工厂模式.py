# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 13:55
"""
简单工厂模式

好处主要有：
1、将创建实例的工作与使用实例的工作分开
2、把初始化实例时的工作放到工厂里进行，使代码更容易维护。
3、使得修改代码时不会引起太大的变动，良好的扩展性。
   比如，有对象A。现在要修改这个实例的方法。就会有对象B，继承A，然后重写A里面的某个方法。这时，如果没有工厂模式，那么就要把每次创建A对象的代码都改为创建B对象。这是很可怕的一件事情。
   如果有工厂模式，那么，我们可以只修改工厂中创建A对象的方法，就可以完成这件事情了。更容易的，可以把这个实例的创建写在配置文件中。那么对于这种变动，只要修改配置文件就可以实现了，不需要修改工厂类。
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


def get_xiaomi_phone(phone_type):
    if phone_type == '5':
        return Xiaomi5()
    elif phone_type == '6':
        return Xiaomi6()


if __name__ == '__main__':
    phone5 = get_xiaomi_phone('5')
    phone5.send_msg()

    phone6 = get_xiaomi_phone('6')
    phone6.send_msg()

    """
    "D:/coding2/python36patterns/创建型模式-简单工厂模式.py:15"  14:16:27  用 小米5 发短信
    "D:/coding2/python36patterns/创建型模式-简单工厂模式.py:23"  14:16:27  用 小米6 发短信
    """
