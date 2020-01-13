# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2020/1/13 0013 12:09
"""
错误使用设计模式的例子

"""
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
    单例模式使用不当，造成项目巨大漏洞，同事说怎么没看到redis生成相关的，因为单例模式一直在db5，同事以为能放到db6，db7，应该使用享元模式，但错误的使用了单例模式。 
    """
    MyRedis(5).set('a',1)
    MyRedis(6).set('b', 2)
    MyRedis(5).set('c', 3)
    MyRedis(6).set('d', 4)

