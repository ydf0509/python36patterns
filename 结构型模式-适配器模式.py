# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 17:39
"""
适配器模式（Adapter Pattern）是作为两个不兼容的接口之间的桥梁。这种类型的设计模式属于结构型模式，它结合了两个独立接口的功能。

这种模式涉及到一个单一的类，该类负责加入独立的或不兼容的接口功能。举个真实的例子，读卡器是作为内存卡和笔记本之间的适配器。您将内存卡插入读卡器，再将读卡器插入笔记本，这样就可以通过笔记本来读取内存卡。

"""
from monkey_print2 import print


class Dog:
    def __init__(self, name):
        self.name = name

    def wangwang(self):
        print('my name is' + self.name + '。。。汪汪汪。。。')

    def dog_run(self):
        print(f'{self.name} is running')


class Cat:
    def __init__(self, name):
        self.name = name

    def miaomiao(self):
        print('my name is' + self.name + '。。。喵喵喵。。。')

    def cat_run(self):
        print(f'{self.name} is running')


class Sheep:
    def __init__(self, name):
        self.name = name

    def miemie(self):
        print('my name is' + self.name + '。。。咩咩。。。')

    def sheet_run(self):
        print(f'{self.name} is running')


class Adapter:
    def __init__(self, adapted_methods):

        self.__dict__.update(adapted_methods)

    def speak(self):
        pass

    def run(self):
        pass


def main():
    animals = []
    dog = Dog('旺财')
    cat = Cat('大脸猫')
    sheep = Sheep('喜洋洋')
    animals.append(Adapter({'speak': dog.wangwang, 'run': dog.dog_run}))
    animals.append(Adapter({'speak': cat.miaomiao, 'run': cat.cat_run}))
    animals.append(Adapter({'speak': sheep.miemie, 'run': sheep.sheet_run}))

    for a in animals:
        a.speak()
        a.run()


if __name__ == "__main__":
    main()
