# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 11:13

"""
中介者模式(Mediator Pattern):用一个对象来封装一系列的对象交互，中介者使各对象不需要显示地相互引用，从而使耦合松散，而且可以独立地改变它们之间的交互.
"""
from monkey_print2 import print
class ChatRoom:
    @staticmethod
    def show_message(user,msg):
        print(f'{user.name} 说： {msg}')

class User:
    def __init__(self,name):
        self.name = name

    def send_msg(self,msg):
        ChatRoom.show_message(self,msg)

if __name__ == '__main__':
    user1 = User('小明')
    user2 = User('小红')
    user1.send_msg('早上好')
    user2.send_msg('晚上好')

    """
    "D:/coding2/python36patterns/行为型模式-中介者模式.py:12"  11:21:04  小明 说： 早上好
"D:/coding2/python36patterns/行为型模式-中介者模式.py:12"  11:21:04  小红 说： 晚上好
    """