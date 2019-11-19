# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/11/19 0019 12:22
from monkey_print2 import print


class FlyweightMetaClass(type):
    def __init__(cls, name, bases, dict):
        super(FlyweightMetaClass, cls).__init__(name, bases, dict)
        cls._instance_map = {}

    @staticmethod
    def _make_arguments_to_key(args, kwds):
        key = args
        if kwds:
            sorted_items = sorted(kwds.items())
            for item in sorted_items:
                key += item
        return key

    def __call__(cls, *args, **kw):
        cache_key = f'{cls}_{cls._make_arguments_to_key(args, kw)}'
        if cache_key not in cls._instance_map:
            cls._instance_map[cache_key] = super().__call__(*args, **kw)
        return cls._instance_map[cache_key]


class A(metaclass=FlyweightMetaClass):
    def __init__(self, a, b):
        print(f'初始化 {a},{b}')


if __name__ == '__main__':
    A(1, 2)
    A(1, 2)
    A(1, 3)
    """
    "D:/coding2/python36patterns/创建型模式-享元模式-元类.py:28"  14:19:44  初始化 1,2
    "D:/coding2/python36patterns/创建型模式-享元模式-元类.py:28"  14:19:44  初始化 1,3
    """
