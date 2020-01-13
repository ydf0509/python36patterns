# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 13:55
"""
享元模式
享元模式通过为相似对象引入数据共享来最小化内存使用，提升性能，一个享元就是一个包含状态的独立的不可变数据的共享对象，依赖状态的可变数据不应是享元的一部分，因为每个对象的这种信息不相同，无法共享，如果享元需要非固有数据应该由客户端代码显示提供。

享元模式介于单例模式和不加控制得多例模式之间。非常灵活，实用性和使用场景大于单例模式。
例如创建一个数据库连接，不希望建立多个连接，但又要在同一解释器下操作好多台机器的数据库，当传参的机器的ip端口不同时候，那肯定要创建一个新的连接了，这种使用享元模式适合。
"""
from monkey_print2 import print


class A:
    pool = dict()

    def __new__(cls, identity):
        """
        假设相同的学号只会有1个学生
        :param identity:
        :return:

        这个是享元模式，有人一看到重写 __new__就条件反射神经过敏，但凡是重写了__new__的代码他都认为是单例模式。
        主要是没有掌握类的一些概念的本质，死记硬背形式造成的错误认知。
        最起码要知道__new__是干啥，__init__是干啥，不知道的话救护死记硬背单例模式的形式。
        """
        obj = cls.pool.get(identity, None)
        if not obj:
            obj = object.__new__(cls)
            print(f'实例化 学号为 {identity} 的学生')
            cls.pool[identity] = obj
        return obj

    def __init__(self, identity):
        self.identity = identity

    def eat(self):
        print(f'{self.identity} 吃饭')

if __name__ == '__main__':
    A('001').eat()
    A('001').eat()
    A('002').eat()

    """
    不会多次生成 001学号的同学这个对象。
    "D:/coding2/python36patterns/创建型模式-享元模式.py:17"  15:29:38  实例化 学号为 001 的学生
    "D:/coding2/python36patterns/创建型模式-享元模式.py:25"  15:29:38  001 吃饭
    "D:/coding2/python36patterns/创建型模式-享元模式.py:25"  15:29:38  001 吃饭
    "D:/coding2/python36patterns/创建型模式-享元模式.py:17"  15:29:38  实例化 学号为 002 的学生
    "D:/coding2/python36patterns/创建型模式-享元模式.py:25"  15:29:38  002 吃饭
    """

