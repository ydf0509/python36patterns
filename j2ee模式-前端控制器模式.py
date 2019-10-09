# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 15:32

"""
前端控制器模式（Front Controller Pattern）是用来提供一个集中的请求处理机制，所有的请求都将由一个单一的处理程序处理。该处理程序可以做认证/授权/记录日志，或者跟踪请求，然后把请求传给相应的处理程序。以下是这种设计模式的实体。

前端控制器（Front Controller） - 处理应用程序所有类型请求的单个处理程序，应用程序可以是基于 web 的应用程序，也可以是基于桌面的应用程序。
调度器（Dispatcher） - 前端控制器可能使用一个调度器对象来调度请求到相应的具体处理程序。
视图（View） - 视图是为请求而创建的对象。

从java转化来，命名规范懒得改了。
"""
from abc import ABCMeta, abstractmethod
from monkey_print2 import print


class HomeView:
    def show(self):
        print('显示 Home 页面')


class StudentView:
    def show(self):
        print('显示 Student 页面')


class Dispatcher:
    def __init__(self):
        self.student_view = StudentView()
        self.home_view = HomeView()

    def dispatch(self, request: str):
        if request.upper() == 'STUDENT':
            self.student_view.show()
        else:
            self.home_view.show()


class FrontController:
    def __init__(self):
        self.__dispatcher = Dispatcher()

    def is_authentic_user(self):
        print("用户鉴权成功")
        return True

    def track_request(self, request):
        print("被请求页面: " + request)

    def dispatch_request(self, request):
        self.track_request(request)
        if self.is_authentic_user():
            self.__dispatcher.dispatch(request)


if __name__ == '__main__':
    front_controller = FrontController()
    front_controller.dispatch_request("HOME")
    front_controller.dispatch_request("STUDENT")

    """
  "D:/coding2/python36patterns/j2ee模式-前端控制器模式.py:49"  16:54:03  被请求页面: HOME
"D:/coding2/python36patterns/j2ee模式-前端控制器模式.py:45"  16:54:03  用户鉴权成功
"D:/coding2/python36patterns/j2ee模式-前端控制器模式.py:20"  16:54:03  显示 Home 页面
"D:/coding2/python36patterns/j2ee模式-前端控制器模式.py:49"  16:54:03  被请求页面: STUDENT
"D:/coding2/python36patterns/j2ee模式-前端控制器模式.py:45"  16:54:03  用户鉴权成功
"D:/coding2/python36patterns/j2ee模式-前端控制器模式.py:25"  16:54:03  显示 Student 页面

    """
