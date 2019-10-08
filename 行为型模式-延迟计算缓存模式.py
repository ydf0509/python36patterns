# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 17:12
"""
23种设计模式中没有提到这一种。
用于执行代价比较大的场景。可以选择永久缓存或者缓存一段时间。

"""
import sys
import time
from functools import wraps

from monkey_print2 import print

class cached_class_property(object):
    """类属性缓存装饰器,把方法的结果缓存为类属性"""

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        if obj is None:
            return self
        value = self.func(obj)
        setattr(cls, self.func.__name__, value)
        return value


# noinspection PyPep8Naming
class cached_instance_property(object):
    """实例属性缓存装饰器，把方法的结果缓存为实例属性"""

    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        print(obj, cls)
        if obj is None:
            return self
        value = obj.__dict__[self.func.__name__] = self.func(obj)
        return value



class FunctionResultCacher:
    """
    使函数的结果缓存指定的时间。例如在5分钟内已经查询了深圳的天气，再次调用查天气的函数直接返回之前查询的天气。

    """
    func_result_dict = {}
    """
    {
        (f1,(1,2,3,4)):(10,1532066199.739),
        (f2,(5,6,7,8)):(26,1532066211.645),
    }
    """

    @classmethod
    def cached_function_result_for_a_time(cls, cache_time: float):
        """
        函数的结果缓存一段时间装饰器,不要装饰在返回结果是超大字符串或者其他占用大内存的数据结构上的函数上面。
        :param cache_time :缓存的时间
        :type cache_time : float
        """

        def _cached_function_result_for_a_time(fun):

            @wraps(fun)
            def __cached_function_result_for_a_time(*args, **kwargs):
                # print(cls.func_result_dict)
                # if len(cls.func_result_dict) > 1024:
                if sys.getsizeof(cls.func_result_dict) > 100 * 1000 * 1000:
                    cls.func_result_dict.clear()

                key = cls._make_arguments_to_key(args, kwargs)
                if (fun, key) in cls.func_result_dict and time.time() - cls.func_result_dict[(fun, key)][1] < cache_time:
                    return cls.func_result_dict[(fun, key)][0]
                else:
                    print('函数 [{}] 此次不能使用缓存'.format(fun.__name__))
                    result = fun(*args, **kwargs)
                    cls.func_result_dict[(fun, key)] = (result, time.time())
                    return result

            return __cached_function_result_for_a_time

        return _cached_function_result_for_a_time

    @staticmethod
    def _make_arguments_to_key(args, kwds):
        key = args
        if kwds:
            sorted_items = sorted(kwds.items())
            for item in sorted_items:
                key += item
        return key  # 元祖可以相加。