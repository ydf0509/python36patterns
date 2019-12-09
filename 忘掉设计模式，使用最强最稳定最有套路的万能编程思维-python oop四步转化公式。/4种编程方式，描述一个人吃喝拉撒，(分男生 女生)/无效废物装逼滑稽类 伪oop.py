# -*- coding: utf-8 -*-
# @Author  : ydf
"""
面向过程写得无效废物类，没有封装，大量rentun，这样写的类没有任何作用。
和person_f文件的写法是一样的。下面这3个类分别为实例方法类 类方法类 静态方法类，但写成了需要反复重复传参和大量return，这3个全部都是废物滑稽类，不是真oop

写这个是为了说明
1、证明我没说过写类就比写函数流弊了，关键要看是不是真oop。
2、写代码时候不能有写类就是高大上的想法，关键看写的类是不是真opp。
"""


class Person:
    def show_weight(self, name, weight):
        print(f'{name} 的体重是： {weight} 千克')

    def show_height(self, xingmin, height):  # xingmin: xingmin也是代表姓名，故意弄成形参不是name，面向过程就会有这种搞不清楚一个参数在不同函数中是不是同一个意义的大缺点。
        print(f'{xingmin} 的身高是： {height} 厘米')

    def grow_weight(self, name, weight, growing_weight):
        weight += growing_weight
        print(f'{name} 的体重增加 {growing_weight} 千克')
        return weight  # 必须把结果return到外部保存

    def grow_height(self, xinmin, height, growing_height):
        print(f'{xinmin} 的身高增加 {growing_height} 厘米')
        height += growing_height
        return height  # 必须把结果return到外部保存

    def pee(self, name, weight):
        """
        因为小便会导致体重发生变化，必须把原来的体重传进来。
        """
        print(f'{name} 蹲着小便')
        return self._reduce_weight_because_of_pee(weight)  # 必须把结果return到外部保存

    def _reduce_weight_because_of_pee(self, tizhong):
        tizhong = tizhong - 0.1  # 体重的别名tizhong和weight是一样的，面向过程不使用实例属性，在很多函数中大量重复传参，形参就会可能不一致，导致看不懂代码。
        return tizhong


class Person2:
    @classmethod
    def show_weight(cls, name, weight):
        print(f'{name} 的体重是： {weight} 千克')

    @classmethod
    def show_height(cls, xingmin, height):  # xingmin: xingmin也是代表姓名，故意弄成形参不是name，面向过程就会有这种搞不清楚一个参数在不同函数中是不是同一个意义的大缺点。
        print(f'{xingmin} 的身高是： {height} 厘米')

    @classmethod
    def grow_weight(cls, name, weight, growing_weight):
        weight += growing_weight
        print(f'{name} 的体重增加 {growing_weight} 千克')
        return weight  # 必须把结果return到外部保存

    @classmethod
    def grow_height(cls, xinmin, height, growing_height):
        print(f'{xinmin} 的身高增加 {growing_height} 厘米')
        height += growing_height
        return height  # 必须把结果return到外部保存

    @classmethod
    def pee(cls, name, weight):
        """
        因为小便会导致体重发生变化，必须把原来的体重传进来。
        """
        print(f'{name} 蹲着小便')
        return cls._reduce_weight_because_of_pee(weight)  # 必须把结果return到外部保存

    @classmethod
    def _reduce_weight_because_of_pee(cls, tizhong):
        tizhong = tizhong - 0.1  # 体重的别名tizhong和weight是一样的，面向过程不使用实例属性，在很多函数中大量重复传参，形参就会可能不一致，导致看不懂代码。
        return tizhong


class Person3:
    @staticmethod
    def show_weight(name, weight):
        print(f'{name} 的体重是： {weight} 千克')

    @staticmethod
    def show_height(xingmin, height):  # xingmin: xingmin也是代表姓名，故意弄成形参不是name，面向过程就会有这种搞不清楚一个参数在不同函数中是不是同一个意义的大缺点。
        print(f'{xingmin} 的身高是： {height} 厘米')

    @staticmethod
    def grow_weight(name, weight, growing_weight):
        weight += growing_weight
        print(f'{name} 的体重增加 {growing_weight} 千克')
        return weight  # 必须把结果return到外部保存

    @staticmethod
    def grow_height(xinmin, height, growing_height):
        print(f'{xinmin} 的身高增加 {growing_height} 厘米')
        height += growing_height
        return height  # 必须把结果return到外部保存

    @staticmethod
    def pee(name, weight):
        """
        因为小便会导致体重发生变化，必须把原来的体重传进来。
        """
        print(f'{name} 蹲着小便')
        return Person3._reduce_weight_because_of_pee(weight)  # 必须把结果return到外部保存

    @staticmethod
    def _reduce_weight_because_of_pee(tizhong):
        tizhong = tizhong - 0.1  # 体重的别名tizhong和weight是一样的，面向过程不使用实例属性，在很多函数中大量重复传参，形参就会可能不一致，导致看不懂代码。
        return tizhong


if __name__ == '__main__':
    """
    person1是无效废物类，因为他改成  person2 person3，下面的调用还能正常运行，所以是个废物类。
    """
    xiaohong = Person3()
    xiaohong_name = '小红'
    xiaohong_height = 110
    xiaohong_weight = 25
    xiaohong.show_height(xiaohong_name, xiaohong_height)
    xiaohong.show_weight(xiaohong_name, xiaohong_weight)
    xiaohong_height = xiaohong.grow_height(xiaohong_name, xiaohong_height, 5)
    xiaohong_weight = xiaohong.grow_weight(xiaohong_name, xiaohong_weight, 1)  # 体重发生了变化，必须把结果return出来保存
    xiaohong.show_height(xiaohong_name, xiaohong_height)
    xiaohong.show_weight(xiaohong_name, xiaohong_weight)  # 展示体重，需要把变化后的体重传进来
    xiaohong_weight = xiaohong.pee(xiaohong_name, xiaohong_weight)  # 连上个厕所都需要把体重参数传进来，然后还要保存新结果，这样大量传参简直不要太low
    xiaohong.show_weight(xiaohong_name, xiaohong_weight)
