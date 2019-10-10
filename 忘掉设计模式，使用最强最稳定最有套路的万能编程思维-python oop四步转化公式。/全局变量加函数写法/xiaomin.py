# -*- coding: utf-8 -*-
# @Author  : ydf

"""
模拟无限复制粘贴扣字low模式
全局变量加函数写法，可以做到少传参 少return，看起来也很简洁，实现简单清晰。
但模块是唯一的，全局变量在模块也是唯一的，无法进行多实例方面的需求，一般都很少这样写，但有不用oop，所以会造成一般喜欢使用频繁return和大量重复传参的写法。

"""

name = '小明'
height = 130
weight = 30


def show_weight():
    print(f'{name} 的体重是： {weight} 千克')


def show_height():
    print(f'{name} 的身高是： {height} 厘米')


def grow_weight(growing_weight):
    global weight
    print(f'{name} 的体重增加 {growing_weight} 千克')
    weight += growing_weight


def grow_height(growing_height):
    global height
    print(f'{name} 的身高增加 {growing_height} 厘米')
    height += growing_height


def pee():
    """
    举个影响属性的例子，上卫生间小便,会导致体重减少。
    :return:
    """
    print(f'{name} 站着小便')
    _reduce_weight_because_of_pee()


def _reduce_weight_because_of_pee():
    global weight
    weight = weight - 0.1


if __name__ == '__main__':
    show_height()
    show_weight()
    grow_height(5)
    grow_weight(1)
    show_height()
    show_weight()
    pee()
    show_weight()

    # REMIND 由于是使用的全局变量，只能完成一个单例的情况，只能完成小明这一个人，无法同时完成小明和小王，如果需要使用小王，必须复制粘贴扣字。
