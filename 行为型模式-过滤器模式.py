# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 14:17
"""
过滤器模式（Filter Pattern）或标准模式（Criteria Pattern）是一种设计模式，这种模式允许开发人员使用不同的标准来过滤一组对象，通过逻辑运算以解耦的方式把它们连接起来。这种类型的设计模式属于结构型模式，它结合多个标准来获得单一标准。
"""
from abc import ABCMeta, abstractmethod
from monkey_print2 import print


class Person:
    def __init__(self, name, sex, marital_status):
        self.name = name
        self.sex = sex
        self.marital_status = marital_status

    def __str__(self):
        return f"""Person: [Name: {self.name}, Gender: {self.sex} Marital Status: {self.marital_status}]"""


class Criteria(metaclass=ABCMeta):
    @abstractmethod
    def meet_criteria(self, persons) -> list:
        pass


class CriteriaMale(Criteria):
    def meet_criteria(self, persons) -> list:
        return [p for p in persons if p.sex.lower() == 'MALE'.lower()]


class CriteriaFemale(Criteria):
    def meet_criteria(self, persons) -> list:
        return [p for p in persons if p.sex.lower() == 'FEMALE'.lower()]


class CriteriaSingle(Criteria):
    def meet_criteria(self, persons) -> list:
        return [p for p in persons if p.sex.lower() == 'SINGLE'.lower()]


class AndCriteria(Criteria):
    def __init__(self, criteria: Criteria, criteria_other: Criteria):
        self.criteria = criteria
        self.criteria_other = criteria_other

    def meet_criteria(self, persons) -> list:
        return self.criteria_other.meet_criteria(self.criteria.meet_criteria(persons))


class OrCriteria(Criteria):
    def __init__(self, criteria: Criteria, criteria_other: Criteria):
        self.criteria = criteria
        self.criteria_other = criteria_other

    def meet_criteria(self, persons) -> list:
        persons1 = self.criteria.meet_criteria(persons)
        persons2 = self.criteria_other.meet_criteria(persons)
        return list(set(persons1 + persons2))


if __name__ == '__main__':
    def print_person_list(p_list):
        for p in p_list:
            print(p)


    person_list = list()
    person_list.append(Person("Robert", "Male", "Single"))
    person_list.append(Person("John", "Male", "Married"))
    person_list.append(Person("Laura", "Female", "Married"))
    person_list.append(Person("Diana", "Female", "Single"))
    person_list.append(Person("Mike", "Male", "Single"))
    person_list.append(Person("Bobby", "Male", "Single"))

    male = CriteriaMale()
    female = CriteriaFemale()
    single = CriteriaSingle()
    singleMale = AndCriteria(single, male)
    singleOrFemale = OrCriteria(single, female)

    print("\nMales: ")
    print_person_list(male.meet_criteria(person_list))

    print("\nFemales: ")
    print_person_list(female.meet_criteria(person_list))

    print("\nSingle Males: ")
    print_person_list(singleMale.meet_criteria(person_list))

    print("\nSingle Or Females: ")
    print_person_list(singleOrFemale.meet_criteria(person_list))
