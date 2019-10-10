# -*- coding: utf-8 -*-
# @Author  : ydf

"""
复制粘贴扣字实现不同之处
演示使用极端面向过程来写，由于没有封装，没有成员变量和全局变量，所以造成需要频繁传参和return.对于实现不同点全盘容易陷入复制文件全流程。
女得有的函数不同。

"""


def show_weight(name, weight):
    print(f'{name} 的体重是： {weight} 千克')


def show_height(xingmin, height):  # xingmin: xingmin也是代表姓名，故意弄成形参不是name，面向过程就会有这种搞不清楚一个参数在不同函数中是不是同一个意义的大缺点。
    print(f'{xingmin} 的身高是： {height} 厘米')


def grow_weight(name, weight, growing_weight):
    weight += growing_weight
    print(f'{name} 的体重增加 {growing_weight} 千克')
    return weight  # 必须把结果return到外部保存


def grow_height(xinmin, height, growing_height):
    print(f'{xinmin} 的身高增加 {growing_height} 厘米')
    height += growing_height
    return height  # 必须把结果return到外部保存


def pee(name, weight):
    """
    因为小便会导致体重发生变化，必须把原来的体重传进来。
    """
    print(f'{name} 蹲着小便')
    return _reduce_weight_because_of_pee(weight)  # 必须把结果return到外部保存


def _reduce_weight_because_of_pee(tizhong):
    tizhong = tizhong - 0.001  # 体重的别名tizhong和weight是一样的，面向过程不使用实例属性，在很多函数中大量重复传参，形参就会可能不一致，导致看不懂代码。
    return tizhong


if __name__ == '__main__':
    xiaohong_name = '小红'
    xiaohong_height = 110
    xiaohong_weight = 25
    show_height(xiaohong_name, xiaohong_height)
    show_weight(xiaohong_name, xiaohong_weight)
    xiaohong_height = grow_height(xiaohong_name, xiaohong_height, 5)
    xiaohong_weight = grow_weight(xiaohong_name, xiaohong_weight, 1)  # 体重发生了变化，必须把结果return出来保存
    show_height(xiaohong_name, xiaohong_height)
    show_weight(xiaohong_name, xiaohong_weight)  # 展示体重，需要把变化后的体重传进来
    xiaohong_weight = pee(xiaohong_name, xiaohong_weight)  # 连上个厕所都需要把体重参数传进来，然后还要保存新结果，这样大量传参简直不要太low
    show_weight(xiaohong_name, xiaohong_weight)


