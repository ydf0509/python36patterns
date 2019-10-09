# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 10:28
"""重要程度 ☆☆☆☆☆
非常简单自然的一种设计模式，说白了就是继承。策略模式说罢了就是组合。
配合oop 4步转化公式，所向披靡，适用范围广。

1.场景：

                        1.1 当多个算法或类实现类似或相同逻辑的时候。

                        1.2 在子类中实现算法有助于减少重复代码的时候。

                        1.3 可以让子类利用覆盖实现行为来定义多个算法的时候。

2.目的：

                        2.1 使用基本操作定义算法的框架。

                        2.2 重新定义子类的某些操作，而无需修改算法的结构。

                        2.3 实现代码重用并避免重复工作

                        2.4 利用通用接口或实现

"""

from abc import ABCMeta, abstractmethod
from monkey_print2 import print


# 抽象方法 AbstractClass
class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    def operation3(self):
        print('操作3')

    #  模板方法 tmplate_method()
    def template_method(self):
        print("Defining the Algorithm.Operation1 follows Operation2")
        self.operation2()
        self.operation1()
        self.operation3()


# 具体类 ConcreteClass
class ConcreteClass(AbstractClass):
    def operation1(self):
        print("My Concrete Operation1")

    def operation2(self):
        print("Operation 2 remains same")


if __name__ == '__main__':
    concreate = ConcreteClass()
    concreate.template_method()

    """
    "D:/coding2/python36patterns/行为型模式-模板模式.py:47"  10:35:10  Defining the Algorithm.Operation1 follows Operation2
"D:/coding2/python36patterns/行为型模式-模板模式.py:59"  10:35:10  Operation 2 remains same
"D:/coding2/python36patterns/行为型模式-模板模式.py:56"  10:35:10  My Concrete Operation1
"D:/coding2/python36patterns/行为型模式-模板模式.py:43"  10:35:10  操作3

    """
