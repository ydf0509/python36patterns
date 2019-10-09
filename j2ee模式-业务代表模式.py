# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 15:32

"""
业务代表模式（Business Delegate Pattern）用于对表示层和业务层解耦。它基本上是用来减少通信或对表示层代码中的业务层代码的远程查询功能。在业务层中我们有以下实体。

客户端（Client） - 表示层代码可以是 JSP、servlet 或 UI java 代码。
业务代表（Business Delegate） - 一个为客户端实体提供的入口类，它提供了对业务服务方法的访问。
查询服务（LookUp Service） - 查找服务对象负责获取相关的业务实现，并提供业务对象对业务代表对象的访问。
业务服务（Business Service） - 业务服务接口。实现了该业务服务的实体类，提供了实际的业务实现逻辑。

从java转化来，命名规范懒得改了。
"""
from abc import ABCMeta, abstractmethod
from monkey_print2 import print


class AbstractBusinessService(metaclass=ABCMeta):
    @abstractmethod
    def doProcessing(self):
        pass


class EJBService(AbstractBusinessService):
    def doProcessing(self):
        print("Processing task by invoking EJB Service")


class JMSService(AbstractBusinessService):
    def doProcessing(self):
        print("Processing task by invoking JMS Service")


def getBusinessService(serviceType: str):
    if serviceType.upper() == 'EJB':
        return EJBService()
    else:
        return JMSService()


class BusinessDelegate:
    def __init__(self):
        self.__businessService = None
        self.__serviceType = None

    def setServiceType(self, serviceType):
        self.__serviceType = serviceType

    def doTask(self):
        businessService = getBusinessService(self.__serviceType)
        businessService.doProcessing()


class Client:
    def __init__(self, businessService: BusinessDelegate):
        self.businessService = businessService

    def doTask(self):
        self.businessService.doTask()


if __name__ == '__main__':
    businessDelegate = BusinessDelegate()
    businessDelegate.setServiceType("EJB")

    client = Client(businessDelegate)
    client.doTask()

    businessDelegate.setServiceType("JMS")
    client.doTask()

    """
    "D:/coding2/python36patterns/j2ee模式-业务代表模式.py:25"  16:07:31  Processing task by invoking EJB Service
    "D:/coding2/python36patterns/j2ee模式-业务代表模式.py:31"  16:07:31  Processing task by invoking JMS Service
    """
