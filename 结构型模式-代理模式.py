# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 22:40

"""
在某些应用中，我们想要在访问某个对象之前执行一个或多个重要的操作，例如，访问敏感
信息——在允许用户访问敏感信息之前，我们希望确保用户具备足够的权限。操作系统中也存在
类似的情况，用户必须具有管理员权限才能在系统中安装新程序。
上面提到的重要操作不一定与安全问题相关。延迟初始化
是另一个案例：我们想要把一个计算成本较高的对象的创建过程延迟到用户首次真正使用它时
才进行。



在代理模式（Proxy Pattern）中，一个类代表另一个类的功能。这种类型的设计模式属于结构型模式。

在代理模式中，我们创建具有现有对象的对象，以便向外界提供功能接口。
"""


class SensitiveInfo:

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))


class Info:

    '''SensitiveInfo的保护代理'''

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()
    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print('unknown option: {}'.format(key))

if __name__ == '__main__':
    main()