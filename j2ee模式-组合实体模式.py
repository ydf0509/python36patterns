"""
组合实体模式（Composite Entity Pattern）用在 EJB 持久化机制中。一个组合实体是一个 EJB 实体 bean，代表了对象的图解。当更新一个组合实体时，内部依赖对象 beans 会自动更新，因为它们是由 EJB 实体 bean 管理的。以下是组合实体 bean 的参与者。

组合实体（Composite Entity） - 它是主要的实体 bean。它可以是粗粒的，或者可以包含一个粗粒度对象，用于持续生命周期。
粗粒度对象（Coarse-Grained Object） - 该对象包含依赖对象。它有自己的生命周期，也能管理依赖对象的生命周期。
依赖对象（Dependent Object） - 依赖对象是一个持续生命周期依赖于粗粒度对象的对象。
策略（Strategies） - 策略表示如何实现组合实体。
"""
from monkey_print2 import print


class DependentObject1:
    def __init__(self):
        self.__data = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data


class DependentObject2:
    def __init__(self):
        self.__data = None

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data


class CoarseGrainedObject:
    def __init__(self):
        self.do1 = DependentObject1()
        self.do2 = DependentObject2()

    def set_data(self, data1, data2):
        self.do1.set_data(data1)
        self.do2.set_data(data2)

    def get_data(self):
        return self.do1.get_data(), self.do2.get_data()


class CompositeEntity:
    def __init__(self):
        self.cgo = CoarseGrainedObject()

    def set_data(self, data1, data2):
        self.cgo.set_data(data1, data2)

    def get_data(self):
        return self.cgo.get_data()


class Client:
    def __init__(self):
        self.compositeEntity = CompositeEntity()

    def print_data(self):
        for data in self.compositeEntity.get_data():
            print(f'Data: {data}')

    def set_data(self, data1, data2):
        self.compositeEntity.set_data(data1, data2)


if __name__ == '__main__':
    client = Client()
    client.set_data("Test", "Data")
    client.print_data()

    client.set_data("Second Test", "Data2")
    client.print_data()

    """
    "D:/coding2/python36patterns/j2ee模式-组合实体模式.py:64"  16:31:51  Data: Test
"D:/coding2/python36patterns/j2ee模式-组合实体模式.py:64"  16:31:51  Data: Data
"D:/coding2/python36patterns/j2ee模式-组合实体模式.py:64"  16:31:51  Data: Second Test
"D:/coding2/python36patterns/j2ee模式-组合实体模式.py:64"  16:31:51  Data: Data2
    """
