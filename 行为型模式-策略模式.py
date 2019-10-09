# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 10:12
"""重要程度 ☆☆☆☆

策略模式（Strategy pattern）鼓励使用多种算法来解决一个问题，其杀手级特性是能够在运
行时透明地切换算法（客户端代码对变化无感知）。因此，如果你有两种算法，并且知道其中一
种对少量输入效果更好，另一种对大量输入效果更好，则可以使用策略模式在运行时基于输入数
据决定使用哪种算法

以下演示策略类。在python中函数也是一等公民。简单情况下的策略模式将函数本身作为另一个函数/方法的入参即可。

"""

from monkey_print2 import print

# 策略模式
class Strategy():
    def process(self):
        pass


class FaultStrategy(Strategy):
    def process(self):
        print("fault")


class NormalStrategy(Strategy):
    def process(self):
        print("normal")


class Park():
    def __init__(self, strategy):
        self.__strategy = strategy

    def geoProcess(self):
        self.__strategy.process()


if __name__ == '__main__':
    p = Park(NormalStrategy())
    p.geoProcess()
    p = Park(FaultStrategy())
    p.geoProcess()

    """
    "D:/coding2/python36patterns/行为型模式-策略模式.py:30"  10:23:25  normal
"D:/coding2/python36patterns/行为型模式-策略模式.py:25"  10:23:25  fault
    """