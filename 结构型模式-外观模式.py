# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 19:00
"""
外观模式（Facade Pattern）隐藏系统的复杂性，并向客户端提供了一个客户端可以访问系统的接口。这种类型的设计模式属于结构型模式，它向现有的系统添加一个接口，来隐藏系统的复杂性。

这种模式涉及到一个单一的类，该类提供了客户端请求的简化方法和对现有系统类方法的委托调用。
"""

from monkey_print2 import print

class A:
    def run(self):
        print('A run')

    def jump(self):
        print('A jump')


class B:
    def run(self):
        print('B run')

    def jump(self):
        print('B jump')


class C:
    def run(self):
        print('C run')

    def jump(self):
        print('C jump')


class Facade:
    def __init__(self):
        self.a = A()
        self.b = B()
        self.c = C()

    def run(self):
        for item in ('a', 'b', 'c'):
            getattr(self, item).run()

    def jump(self):
        for item in ('a', 'b', 'c'):
            getattr(self, item).jump()


if __name__ == '__main__':
    facade = Facade()
    facade.run()
    facade.jump()
