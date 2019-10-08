# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 18:32
"""
函数装饰器
"""
import time
from functools import wraps
from monkey_print2 import print


def timethis(func):
    '''
    Decorator that reports the execution time.
    '''

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


@timethis
def fun():
    time.sleep(3)
    return 1


if __name__ == '__main__':
    fun()
