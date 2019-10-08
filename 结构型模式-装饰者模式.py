# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 18:24

"""
无论何时我们想对一个对象添加额外的功能，都有下面这些不同的可选方法。
 如果合理，可以直接将功能添加到对象所属的类（例如，添加一个新的方法）
 使用组合
 使用继承
与继承相比，通常应该优先选择组合，因为继承使得代码更难复用，继承关系是静态的，并且应用于整个类以及这个类的所有实例（请参考［GOF95，第31页］和网页［t.cn/RqrC8Yo］）。
设计模式为我们提供第四种可选方法，以支持动态地（运行时）扩展一个对象的功能，这种方法就是修饰器。修饰器（Decorator）模式能够以透明的方式（不会影响其他对象）动态地将功能添加到一个对象中（请参考［GOF95，第196页］）。
在许多编程语言中，使用子类化（继承）来实现修饰器模式（请参考［GOF95，第198页］）。
在Python中，我们可以（并且应该）使用内置的修饰器特性。一个Python修饰器就是对Python语法的一个特定改变，用于扩展一个类、方法或函数的行为，而无需使用继承。从实现的角度来说，
Python修饰器是一个可调用对象（函数、方法、类），接受一个函数对象fin作为输入，并返回另一个函数对象 。这意味着可以将任何具有这些属性的可调用对象当作一个修饰器。在第1章和第2章中已经看到如何使用内置的property修饰器让一个方法表现为一个变量。在5.4节，我们将学习如何实现及使用我们自己的修饰器。
修饰器模式和Python修饰器之间并不是一对一的等价关系。Python修饰器能做的实际上比修饰器模式多得多，其中之一就是实现修饰器模式
"""
from monkey_print2 import print

class Foo:
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")


class Foo_decorator:
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print("before run f1")
        self._decoratee.f1()
        print("after run f1")

    def __getattr__(self, name):
        return getattr(self._decoratee, name)

if __name__ == '__main__':
    u = Foo()
    v = Foo_decorator(u)
    v.f1()
    v.f2()