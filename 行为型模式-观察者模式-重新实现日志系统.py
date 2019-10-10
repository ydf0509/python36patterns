# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 9:39

"""重要程度 ☆☆☆
当对象间存在一对多关系时，则使用观察者模式（Observer Pattern）。比如，当一个对象被修改时，则会自动通知它的依赖对象。观察者模式属于行为型模式。
有时，我们希望在一个对象的状态改变时更新另外一组对象。

说这么多抽象的概念，说点具体的就是以日志为例，有人把print当做日志用，里面的区别相当大，日志不仅可以有streamhandler和filehandler，还有mailhandler httphandler
等几亿种自定义handler。logger debug时候自动触发各种handler的emit方法。
用不会日志不理解日志，对logger addHandler各种handler懵逼不知道在干嘛，最主要是不懂观察者模式造成的。
希望举得例子是接近真实有意义，下面简单使用观察者模式重新模拟实现一个伪日志包。
"""
import abc
from monkey_print2 import print


class AbstractHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def emit(self, record):
        pass


class Logger:
    def __init__(self, logger_name):
        self.name = logger_name
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def log(self, record: str):
        for hr in self.handlers:
            hr.emit(f'{self.name} -- {record}')


class StreamHandler(AbstractHandler):
    def emit(self, record):
        print(f' {record}  控制台打印')


class FileHandler(AbstractHandler):
    def emit(self, record):
        print(f' {record}  文件写入')  # 只是为了演示写入文件，用print模拟的伪实现。希望要搞清楚这里的目的不是print。


class MailHandler(AbstractHandler):
    def emit(self, record):
        print(f' {record} 发邮件给某人')  # 只是为了演示发邮件，用print模拟的伪实现。希望要搞清楚这里的目的不是print。


class DingdingHandler(AbstractHandler):
    def emit(self, record):
        print(f' {record} 钉钉机器人将这句话发给群里')  # 只是为了演示发钉钉机器人消息，用print模拟的伪实现。希望要搞清楚这里的目的不是print。


if __name__ == '__main__':
    logger1 = Logger('a')
    logger1.add_handler(StreamHandler())
    logger1.add_handler(FileHandler())
    logger1.add_handler(MailHandler())
    logger1.log('啦啦啦啦啦啦')

    logger2 = Logger('b')
    logger2.add_handler(StreamHandler())
    logger2.add_handler(DingdingHandler())
    logger2.log('哈哈哈哈哈哈')

    """
    可以看到日志非常灵活，可以按需选择几个handler，例如日志a会 控制台打印版 写入文件 发邮件，日志b控制台打印 发钉钉消息。
    "D:/coding2/python36patterns/行为型模式-观察者模式.py:36"  10:00:19   a -- 啦啦啦啦啦啦  控制台打印
    "D:/coding2/python36patterns/行为型模式-观察者模式.py:40"  10:00:19   a -- 啦啦啦啦啦啦  文件写入
    "D:/coding2/python36patterns/行为型模式-观察者模式.py:45"  10:00:19   a -- 啦啦啦啦啦啦 发邮件给某人
    "D:/coding2/python36patterns/行为型模式-观察者模式.py:36"  10:00:19   b -- 哈哈哈哈哈哈  控制台打印
    "D:/coding2/python36patterns/行为型模式-观察者模式.py:49"  10:00:19   b -- 哈哈哈哈哈哈 钉钉机器人将这句话发给群里
    """
