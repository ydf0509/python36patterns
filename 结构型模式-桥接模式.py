# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 17:39
"""
桥接，是像一座桥连接两岸，而Python程序设计中的桥接指的是抽象部分和实体部分的连接，简单来说是类和类实例化过称中的连接。

桥接模式通过在类和类实例化中间作用，使其抽象和实现可以独立变化而不互相干扰，这就是桥接模式最大的作用。

核心的思想是通过封装，将一个抽象类的相关参数和方法分别作为桥接类的属性，这样在实例化桥接类后通过修改桥接类的属性，便可以实现抽象和实现之间的独立变化。

"""
from monkey_print2 import print


class A:
    def run(self, name):
        print("my name is :{}".format(name))


class B:
    def run(self, name):
        print("我的名字是：{}".format(name))


class Bridge:
    def __init__(self, ager, classname):
        self.ager = ager
        self.classname = classname

    def bridge_run(self):
        self.classname.run(self.ager)


if __name__ == '__main__':
    test = Bridge('李华', A())
    test.bridge_run()
    test.ager = 'Tome'
    test.bridge_run()
    test.classname = B()
    test.bridge_run()
    test.ager = '李华'
    test.bridge_run()
    """
    "D:/coding2/python36patterns/结构型模式-桥接模式.py:7"  17:56:50  my name is :李华
"D:/coding2/python36patterns/结构型模式-桥接模式.py:7"  17:56:50  my name is :Tome
"D:/coding2/python36patterns/结构型模式-桥接模式.py:12"  17:56:50  我的名字是：Tome
"D:/coding2/python36patterns/结构型模式-桥接模式.py:12"  17:56:50  我的名字是：李华

    """
