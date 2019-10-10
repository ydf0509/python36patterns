# -*- coding: utf-8 -*-
# @Author  : ydf
"""
封装的工具类没有发明非常实用的好功能，全都是自己取个新的方法名字调用官方的方法，没什么卵用，还要新记忆各种新的名字。还不如直接调用官方的算了。
比如套上享元模式 单例模式或者缓存模式来控制创建，或者在官方基础上增加个自动聚合数据库命令的，这样才可以，这样才有作用。
"""
from redis import Redis
class CustomRedis():
    def __init__(self,host,port):
        self._r = Redis(host,port)

    def my_exists(self,name):
        return  self._r.exists(name)

    def my_hget(self,name,key):
        return self._r.hget(name,key)

    def my_sadd(self,name,value):
        return self._r.sadd(name,value)

    def my_lpush(self,name,value):
        return self._r.sadd(name,value)

    # 。。。。。。。。。。。。。。。。。。