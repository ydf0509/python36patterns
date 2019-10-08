# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 13:55
"""
建造者模式

建造者模式
建造者模式（Builder Pattern）使用多个简单的对象一步一步构建成一个复杂的对象。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。

一个 Builder 类会一步一步构造最终的对象。该 Builder 类是独立于其他对象的。

介绍
意图：将一个复杂的构建与其表示相分离，使得同样的构建过程可以创建不同的表示。

主要解决：主要解决在软件系统中，有时候面临着"一个复杂对象"的创建工作，其通常由各个部分的子对象用一定的算法构成；由于需求的变化，这个复杂对象的各个部分经常面临着剧烈的变化，但是将它们组合在一起的算法却相对稳定。

何时使用：一些基本部件不会变，而其组合经常变化的时候。

如何解决：将变与不变分离开。

关键代码：建造者：创建和提供实例，导演：管理建造出来的实例的依赖关系。

应用实例： 1、去肯德基，汉堡、可乐、薯条、炸鸡翅等是不变的，而其组合是经常变化的，生成出所谓的"套餐"。 2、JAVA 中的 StringBuilder。

优点： 1、建造者独立，易扩展。 2、便于控制细节风险。

缺点： 1、产品必须有共同点，范围有限制。 2、如内部变化复杂，会有很多的建造类。

使用场景： 1、需要生成的对象具有复杂的内部结构。 2、需要生成的对象内部属性本身相互依赖。

注意事项：与工厂模式的区别是：建造者模式更加关注与零件装配的顺序。
"""
from monkey_print2 import print

import abc


# 步骤一：创建对应的产品抽象类/产品类
class Building(object):
    def __init__(self):
        self.floor = None
        self.size = None

    def __repr__(self):
        return 'Floor: {0.floor} | size: {0.size}'.format(self)


# 步骤三：创建构建者抽象类，主要是定义构建者通用属性/方法，以及继承者必须实现的功能抽象
# Abstract builder
class AbsBuilder(object):
    def __init__(self):
        self.building = None

    def new_building(self):
        self.building = Building()

    @abc.abstractmethod
    def build_floor(self):
        pass

    @abc.abstractmethod
    def build_size(self):
        pass


# 步骤四：具体构建者类实现
class HouseBuilder(AbsBuilder):
    def build_floor(self):
        self.building.floor = 'one'

    def build_size(self):
        self.building.size = '220 squre'


class FlatBuilder(AbsBuilder):
    def build_floor(self):
        self.building.floor = 'seven'

    def build_size(self):
        self.building.size = '140 squre'


# 步骤二：创建产品的指挥者类，即最终提供给客户端的产品的实例对象，以及组装过程
class Director(object):
    def __init__(self):
        self.builder = None

    def construct_building(self):
        """
        #建造者模式下，仅在需要时客户端代码才显式地请求指挥者返回最终的对象
        """
        self.builder.new_building()
        self.builder.build_floor()
        self.builder.build_size()

    def get_building(self):
        return self.builder.building


class Client(object):
    def build(self, build_type):
        if build_type == "House":
            director = Director()
            builder = HouseBuilder()
            director.builder = builder
            director.construct_building()
            building = director.get_building()
            print(building)
        else:
            director = Director()
            builder = FlatBuilder()
            director.builder = builder
            director.construct_building()
            building = director.get_building()
            print(building)


if __name__ == "__main__":
    build_type = "Flat"
    client = Client()
    client.build(build_type)
