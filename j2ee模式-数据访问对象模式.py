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


class Student:
    def __init__(self, name, roll_no):
        self.__name = name
        self.__roll_no = roll_no

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, roll_no):
        self.__roll_no = roll_no


class AbstractStudentDao(metaclass=ABCMeta):
    @abstractmethod
    def get_all_students(self):
        pass

    def get_student(self, roll_num):
        pass

    def update_student(self, student: Student):
        pass

    def delete_student(self, student: Student):
        pass


class StudentDao(AbstractStudentDao):
    def __init__(self):
        self.students = []
        student1 = Student("小明", 0)
        student2 = Student("小黄", 1)
        self.students.append(student1)
        self.students.append(student2)

    def get_all_students(self):
        return self.students

    def get_student(self, roll_num):
        return self.students[roll_num]

    def update_student(self, student: Student):
        # print(student.get_roll_no())
        # print(student.get_name())
        self.students[student.get_roll_no()].set_name(student.get_name())
        print("Student: RollNo " + str(student.get_roll_no())
              + ", updated in the database")

    def delete_student(self, student: Student):
        self.students.pop(student.get_roll_no())
        print("Student: Roll No " + str(student.get_roll_no())
              + ", deleted from database")


if __name__ == '__main__':

    student_dao = StudentDao()

    # // 输出所有的学生
    for student in student_dao.get_all_students():
        print("Student: [RollNo : " + str(student.get_roll_no()) + ", Name : " + student.get_name() + " ]")

    # // 更新学生
    student = student_dao.get_all_students()[0]
    student.set_name("Michael")
    student_dao.update_student(student)

    # // 获取学生
    student_dao.get_student(0)
    print("Student: [RollNo : "
          + str(student.get_roll_no()) + ", Name : " + student.get_name() + " ]")

    """
    "D:/coding2/python36patterns/j2ee模式-数据访问对象模式.py:84"  17:38:06  Student: [RollNo : 0, Name : 小明 ]
"D:/coding2/python36patterns/j2ee模式-数据访问对象模式.py:84"  17:38:06  Student: [RollNo : 1, Name : 小黄 ]
"D:/coding2/python36patterns/j2ee模式-数据访问对象模式.py:70"  17:38:06  Student: RollNo 0, updated in the database
"D:/coding2/python36patterns/j2ee模式-数据访问对象模式.py:94"  17:38:06  Student: [RollNo : 0, Name : Michael ]
    """
