# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 15:32

"""
数据访问对象模式（Data Access Object Pattern）或 DAO 模式用于把低级的数据访问 API 或操作从高级的业务服务中分离出来。以下是数据访问对象模式的参与者。

数据访问对象接口（Data Access Object Interface） - 该接口定义了在一个模型对象上要执行的标准操作。
数据访问对象实体类（Data Access Object concrete class） - 该类实现了上述的接口。该类负责从数据源获取数据，数据源可以是数据库，也可以是 xml，或者是其他的存储机制。
模型对象/数值对象（Model Object/Value Object） - 该对象是简单的 POJO，包含了 get/set 方法来存储通过使用 DAO 类检索到的数据。
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
