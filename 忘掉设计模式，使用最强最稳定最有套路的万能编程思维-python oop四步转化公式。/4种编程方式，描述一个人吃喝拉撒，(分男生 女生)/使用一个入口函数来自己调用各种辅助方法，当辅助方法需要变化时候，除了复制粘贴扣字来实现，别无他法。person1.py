# -*- coding: utf-8 -*-
# @Author  : ydf

"""
实现一个人的   长身体 小便 的功能。
模拟常见的价格解析，n多个辅助函数，然后暴露一个公有函数供外部调用，这样无需在调用处写好几行调用各种证件辅助方法和保存各种证件变量。但是当某个辅助函数需要改变时候，除了全盘复制粘贴扣字，还有什么办法？
如果没办法，那就是又会变成使用无限复制粘贴low模式了。

"""


def _show_weight(name, weight):
    print(f'{name} 的体重是： {weight} 千克')


def _show_height(xingmin, height):  # xingmin: xingmin也是代表姓名，故意弄成形参不是name，面向过程就会有这种搞不清楚一个参数在不同函数中是不是同一个意义的大缺点。
    print(f'{xingmin} 的身高是： {height} 厘米')


def _grow_weight(name, weight, growing_weight):
    weight += growing_weight
    print(f'{name} 的体重增加 {growing_weight} 千克')
    return weight  # 必须把结果return到外部保存


def _grow_height(xinmin, height, growing_height):
    print(f'{xinmin} 的身高增加 {growing_height} 厘米')
    height += growing_height
    return height  # 必须把结果return到外部保存


def _pee(name, weight):
    """
    因为小便会导致体重发生变化，必须把原来的体重传进来。
    """
    print(f'{name} 站着小便')  # REMIND 如果是女得，这个函数需要修改成 蹲着小便。
    return __reduce_weight_because_of_pee(name, weight)  # 必须把结果return到外部保存


def __reduce_weight_because_of_pee(name, tizhong):
    # 小便后会导致体重减少。
    tizhong = _grow_weight(name, tizhong, growing_weight=-0.1)  # 体重的别名tizhong和weight是一样的，面向过程不使用实例属性，在很多函数中大量重复传参，形参就会可能不一致，导致看不懂代码。
    return tizhong


def public_main_function(name, weight, height):  # 写一个公有入口函数，自己调用身高增加函数  体重增加函数  上卫生间小便的函数，一般现在的代码都是这样弄得，这样在外部调用时候调用入口函数就可以了。
    height = _grow_height(name, height, 5)
    weight = _grow_weight(name, weight, 1)
    weight = _pee(name, weight)  # 如果要实现pee函数不同之处，面向过程时候这里也要改。
    _show_height(name, height)
    _show_weight(name, weight)
    return weight, height


if __name__ == '__main__':
    result = public_main_function('小明', 30, 120)
    print(result)
    """
    这样可以不在外部写很多行来调用辅助函数，和写很多中间变量在外部给多个辅助函数传来传去的。但有三个大毛病是
    1.写法曲折，虽然提供了一个入口函数，但还是在入口函数里面内部反复return和传参，思路不直观。没有在一组函数中操纵全局变量的那种写法思路清晰。
    2、现在要使用小红怎么办？增加一个女孩的_pee函数  (_pee_girl)，还要增加一个调用女孩pee函数的 public_main_function函数(public_main_function_girl)。这样会导致函数名不一致，调用不一致,又增加调用难度。
    3、如果不新增和修改函数名，假设此模块名字是person1.py那就只能新增能一个模块person2.py,然后全盘复制粘贴person1.py,然后将_pee函数里面扣字，这样调用 person1.public_main_function() 就和 person2.public_main_function() 
    具有调用方式上有一致性，也实现了男女的小便不同之处，但为了一个小的不同，而去复制粘贴全流程，然后扣字，这样简直不要太low，每当需要修改某个地方时候，这两个文件都需要去修改一下。复制粘贴扣字两三次还好，要是复制粘贴扣字几百次，那就很伤心了。酒店里面调度不同函数比价的文件夹里面连续重复20多个文件，所有文件代码布局外观一眼看起来具有99%相似性，就是这种原因导致写成那样的。
    只有使用oop才能很好解决这几个弊端。写代码慢，写代码复杂难懂，写得无限重复相似 就是排斥oop和过分喜爱极端面向过程写法导致的。
    """
