# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 13:55
"""
单例模式
适用范围三颗星，这不是最常用的设计模式。往往只能脱出而出仅仅能说出这一种设计模式，但oop根本目的是要多例，
使用oop来实现单例模式，好处包括
1 延迟初始化（只有在生成对象时候调用__init__里面时候才进行初始化）
2 动态传参初始化
否则，一般情况下，不需要来使用类来搞单例模式，文件级模块全局变量的写法搞定即可，python模块天然单例，不信的话可以测试一下，c导入a，b也导入a，c导入b，在a里面直接print hello，
运行c.py,只会看到一次print hello。

"""
import threading
from functools import wraps

from monkey_print2 import print


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance


class A(metaclass=Singleton):
    def __init__(self, identity):
        print('执行init')
        self.identity = identity

    def eat(self):
        print(f'{self.identity} 吃饭')


if __name__ == '__main__':
    a1 = A('001')
    a2 = A('001')
    print(a1 == a2)
    a1.eat()
    a2.eat()
    a3 = A('003')
    print(a1 == a3)
    a3.eat()

    """
    a1 a2 a3 三次实例化出来，但都是同一个对象。对比下享元模式。
    "D:/coding2/python36patterns/创建型模式-单例模式.py:36"  16:00:25  True
"D:/coding2/python36patterns/创建型模式-单例模式.py:30"  16:00:25  001 吃饭
"D:/coding2/python36patterns/创建型模式-单例模式.py:30"  16:00:25  001 吃饭
"D:/coding2/python36patterns/创建型模式-单例模式.py:40"  16:00:25  True
"D:/coding2/python36patterns/创建型模式-单例模式.py:30"  16:00:25  001 吃饭
    """
