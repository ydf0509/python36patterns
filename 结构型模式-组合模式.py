# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 17:39
"""
组合模式
组合模式（Composite Pattern），又叫部分整体模式，是用于把一组相似的对象当作一个单一的对象。组合模式依据树形结构来组合对象，用来表示部分以及整体层次。这种类型的设计模式属于结构型模式，它创建了对象组的树形结构。

这种模式创建了一个包含自己对象组的类。该类提供了修改相同对象组的方式。

我们通过下面的实例来演示组合模式的用法。实例演示了一个组织中员工的层次结构。

介绍
意图：将对象组合成树形结构以表示"部分-整体"的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性。

主要解决：它在我们树型结构的问题中，模糊了简单元素和复杂元素的概念，客户程序可以向处理简单元素一样来处理复杂元素，从而使得客户程序与复杂元素的内部结构解耦。

何时使用： 1、您想表示对象的部分-整体层次结构（树形结构）。 2、您希望用户忽略组合对象与单个对象的不同，用户将统一地使用组合结构中的所有对象。

如何解决：树枝和叶子实现统一接口，树枝内部组合该接口。

关键代码：树枝内部组合该接口，并且含有内部属性 List，里面放 Component。

应用实例： 1、算术表达式包括操作数、操作符和另一个操作数，其中，另一个操作符也可以是操作数、操作符和另一个操作数。 2、在 JAVA AWT 和 SWING 中，对于 Button 和 Checkbox 是树叶，Container 是树枝。

优点： 1、高层模块调用简单。 2、节点自由增加。

缺点：在使用组合模式时，其叶子和树枝的声明都是实现类，而不是接口，违反了依赖倒置原则。

使用场景：部分、整体场景，如树形菜单，文件、文件夹的管理。

注意事项：定义时为具体类。

"""
from monkey_print2 import print


# Component：公司抽象类
class Company:
    name = ''

    def __init__(self, name):
        self.name = name

    def add(self, company):
        pass

    def remove(self, company):
        pass

    def display(self, depth):
        pass

    def line_of_duty(self):  # 履行职责
        pass

    # Composite：公司类


class ConcreteCompany(Company):
    childrenCompany = None

    def __init__(self, name):
        Company.__init__(self, name)
        self.childrenCompany = []

    def add(self, company):
        self.childrenCompany.append(company)

    def remove(self, company):
        self.childrenCompany.remove(company)

    def display(self, depth):
        print('-' * depth + self.name)

        for component in self.childrenCompany:
            component.display(depth + 2)

    def line_of_duty(self):  # 履行职责
        for component in self.childrenCompany:
            component.line_of_duty()


# Leaf：具体职能部门
class HRDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)

    def display(self, depth):
        print('-' * depth + self.name)

    def line_of_duty(self):  # 履行职责
        print('%s\t员工招聘培训管理' % self.name)


# Leaf：具体职能部门
class FinanceDepartment(Company):
    def __init__(self, name):
        Company.__init__(self, name)

    def display(self, depth):
        print('-' * depth + self.name)

    def line_of_duty(self):  # 履行职责
        print('%s\t公司财务收支管理' % self.name)




if __name__ == '__main__':
    root = ConcreteCompany('北京总公司')
    root.add(HRDepartment('总公司人力资源部'))
    root.add(FinanceDepartment('总公司财务部'))

    comp = ConcreteCompany('华东分公司')
    comp.add(HRDepartment('华东分公司人力资源部'))
    comp.add(FinanceDepartment('华东分公司财务部'))
    root.add(comp)

    comp1 = ConcreteCompany('南京办事处')
    comp1.add(HRDepartment('南京办事处人力资源部'))
    comp1.add(FinanceDepartment('南京办事处财务部'))
    comp.add(comp1)

    comp2 = ConcreteCompany('杭州办事处')
    comp2.add(HRDepartment('杭州办事处人力资源部'))
    comp2.add(FinanceDepartment('杭州办事处财务部'))
    comp.add(comp2)

    print('-------公司结构图-------')
    root.display(1)

    print('\n-------职责-------')
    root.line_of_duty()


