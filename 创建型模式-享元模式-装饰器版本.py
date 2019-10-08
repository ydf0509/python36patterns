# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 13:55
"""
享元模式
享元模式通过为相似对象引入数据共享来最小化内存使用，提升性能，一个享元就是一个包含状态的独立的不可变数据的共享对象，依赖状态的可变数据不应是享元的一部分，因为每个对象的这种信息不相同，无法共享，如果享元需要非固有数据应该由客户端代码显示提供。

享元模式介于单例模式和不加控制得多例模式之间。非常灵活，实用性和使用场景大于单例模式。
例如创建一个数据库连接，不希望建立多个连接，但又要在同一解释器下操作好多台机器的数据库，当传参的机器的ip端口不同时候，那肯定要创建一个新的连接了，这种使用享元模式适合。
"""
from functools import wraps

from monkey_print2 import print


def flyweight(cls):
    _instance = {}

    def _make_arguments_to_key(args, kwds):
        key = args
        if kwds:
            sorted_items = sorted(kwds.items())
            for item in sorted_items:
                key += item
        return key

    @wraps(cls)
    def _flyweight(*args, **kwargs):
        cache_key = f'{cls}_{_make_arguments_to_key(args, kwargs)}'
        if cache_key not in _instance:
            _instance[cache_key] = cls(*args, **kwargs)
        return _instance[cache_key]

    return _flyweight


@flyweight
class A:
    def __init__(self, identity):
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
    a1和a2是同一个对象，
    "D:/coding2/python36patterns/创建型模式-享元模式-装饰器版本.py:49"  15:48:38  True
    "D:/coding2/python36patterns/创建型模式-享元模式-装饰器版本.py:43"  15:48:38  001 吃饭
    "D:/coding2/python36patterns/创建型模式-享元模式-装饰器版本.py:43"  15:48:38  001 吃饭
    "D:/coding2/python36patterns/创建型模式-享元模式-装饰器版本.py:53"  15:48:38  False
    "D:/coding2/python36patterns/创建型模式-享元模式-装饰器版本.py:43"  15:48:38  003 吃饭
    """
