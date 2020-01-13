# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 13:55
"""
享元模式
享元模式通过为相似对象引入数据共享来最小化内存使用，提升性能，一个享元就是一个包含状态的独立的不可变数据的共享对象，依赖状态的可变数据不应是享元的一部分，因为每个对象的这种信息不相同，无法共享，如果享元需要非固有数据应该由客户端代码显示提供。

享元模式介于单例模式和不加控制得多例模式之间。非常灵活，实用性和使用场景大于单例模式。
例如创建一个数据库连接，不希望建立多个连接，但又要在同一解释器下操作好多台机器的数据库，当传参的机器的ip端口不同时候，那肯定要创建一个新的连接了，这种使用享元模式适合。


例如原理有个同事写的代码是
# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2020/1/13 0013 12:09
"""
# 错误使用单例设计模式的例子

'''
from redis import Redis
class MyRedis:
    _inst = None

    def __new__(cls, *args, **kwargs):
        if not cls._inst:
            self = super().__new__(cls)
            self.__my_init__(*args, **kwargs)
            cls._inst = self
        return cls._inst


    def __my_init__(self,redis_db):
        print(f'传入的redis db是 {redis_db}')
        self.r = Redis(host='127.0.0.1',port=6379,db=redis_db)

    def set(self,key,value):
        self.r.set(key,value)

if __name__ == '__main__':
    """
    单例模式使用不当，造成项目巨大漏洞，同事说怎么没看到redis生成相关的，因为单例模式一直在db5，同事以为能放到db6，db7，应该使用享元模式，单错误的使用了单例模式。 
    """
    MyRedis(5).set('a',1)
    MyRedis(6).set('b', 2)
    MyRedis(5).set('c', 3)
    MyRedis(6).set('d', 4)

'''
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
        最起码要知道__new__是干啥，__init__是干啥，不知道的话就会死记硬背单例模式的形式。
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

    # 下面是关于这个享元模式被人说成是单例模式的反驳。如果是单例模式print(id(A('001')) == id(A('002'))) 结果会是True
    print(id(A('001')) == id(A('002')))  # False
    print(id(A('001')) == id(A('001')))  # True

    """
    不会多次生成 001学号的同学这个对象。
    "D:/coding2/python36patterns/创建型模式-享元模式.py:30"  11:46:53  实例化 学号为 001 的学生
    "D:/coding2/python36patterns/创建型模式-享元模式.py:38"  11:46:53  001 吃饭
    "D:/coding2/python36patterns/创建型模式-享元模式.py:38"  11:46:53  001 吃饭
    "D:/coding2/python36patterns/创建型模式-享元模式.py:30"  11:46:53  实例化 学号为 002 的学生
    "D:/coding2/python36patterns/创建型模式-享元模式.py:38"  11:46:53  002 吃饭
    "D:/coding2/python36patterns/创建型模式-享元模式.py:45"  11:46:53  False
    "D:/coding2/python36patterns/创建型模式-享元模式.py:46"  11:46:53  True
    """
