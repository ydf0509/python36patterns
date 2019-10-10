# -*- coding: utf-8 -*-
# @Author  : ydf

"""
演示使用极端面向过程来写，由于没有封装，没有成员变量和全局变量，所以造成需要在多个函数中频繁重复传参和return
无论是实现还是调用都更为复杂。
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
    print(f'{name} 站着小便')
    return _reduce_weight_because_of_pee(weight)  # 必须把结果return到外部保存


def _reduce_weight_because_of_pee(tizhong):
    tizhong = tizhong - 0.1  # 体重的别名tizhong和weight是一样的，面向过程不使用实例属性，在很多函数中大量重复传参，形参就会可能不一致，导致看不懂代码。
    return tizhong


if __name__ == '__main__':
    # 极端面向过程不仅需要导致频繁传参和return，还要在调用时候设置很多个外部变量来保存状态，如果属性/状态越多，需要外部保存的变量就越多。
    xiaomin_name = '小明'
    xioamin_height = 120
    xiaomin_weight = 30
    show_height(xiaomin_name, xioamin_height)
    show_weight(xiaomin_name, xiaomin_weight)
    xioamin_height = grow_height(xiaomin_name, xioamin_height, 5)
    xiaomin_weight = grow_weight(xiaomin_name, xiaomin_weight, 1)  # 体重发生了变化，必须把结果return出来保存
    show_height(xiaomin_name, xioamin_height)
    show_weight(xiaomin_name, xiaomin_weight)  # 展示体重，需要把变化后的体重传进来
    xiaomin_weight = pee(xiaomin_name, xiaomin_weight)  # 连上个厕所都需要把体重参数传进来，这样大量传参简直不要太low
    show_weight(xiaomin_name, xiaomin_weight)

    print('& ' * 100)

    # 频繁重复传参和retutn主要是为了多实例，不然全局变量加函数就搞定了。演示面向过程实现多实例的需求，由于各种变量都是在调用地方传入和保存，所以这种面向过程的地方可以实现多实例，为了实现多实例导致重复传参和频繁return，导致代码无论在本身实现写法还是调用上，都极为复杂。例如演示这种方式实现多实例小王

    # xiaowang_name = '小王'
    # xioamin_height = 130
    # xiaowang_weight = 35
    # show_height(xiaowang_name, xioamin_height)
    # show_weight(xiaowang_name, xiaowang_weight)
    # xioamin_height = grow_height(xiaowang_name, xioamin_height, 6)
    # xiaowang_weight = grow_weight(xiaowang_name, xiaowang_weight, 2)
    # show_height(xiaowang_name, xioamin_height)
    # show_weight(xiaowang_name, xiaowang_weight)
    # xiaowang_weight = pee(xiaowang_name, xiaowang_weight)
    # show_weight(xiaowang_name, xiaowang_weight)

    # 这样的写法，如果要实现小红，那就十分麻烦了，因为小红的pee函数肯定不能这么运行。如果直接在此处修改函数,那代码就不能兼容小明 小王。导致又要全盘复制文件，庵后扣字，来重写pee函数。
