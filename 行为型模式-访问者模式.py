# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 11:31

"""
1。为什么要使用设计模式？
从理论上来说，设计模式是对程序问题比较好的解决方案。无数的程序员都曾经遇到过这些问题，并且他们使用这些解决方案去处理这些问题。所以当你遇到同样的问题，为什么要去想着创建一个解决方案而不是用现成的并且被证明是有效的呢？



2。访问者模式解决了什么问题？
1)对象结构中对象对应的类很少改变，但经常需要在此对象结构上定义新的操作。
2)需要对一个对象结构中的对象进行很多不同的并且不相关的操作，而需要避免让这些操作”污染”这些对象的类，也不希望在增加新操作时修改这些类。



3。访问者模式使用场景
1)对象结构比较稳定，但经常需要在此对象结构上定义新的操作

2)需要对一个对象结构中的对象进行很多不同的且不相关的操作，而需要避免这些操作“污染”这些对象的类，也不希望在增加新操作时修改这些类。

比如：访问者可以对功能进行统一，可以做报表、UI、拦截器与过滤器。



数据类只提供一个数据处理的接口，而数据类的处理方法我们叫它访问者

下面例子可以实现：安排不同年份的财务报表给不同的角色分析，这就是访问者模式的魅力；访问者模式的核心是在保持原有数据结构的基础上，实现多种数据的处理方法，该方法的角色就是访问者。



4。访问者模式优点
1)使得数据结构和作用于结构上的操作解耦，使得操作集合可以独立变化。

2)添加新的操作或者说访问者会非常容易。

3)将对各个元素的一组操作集中在一个访问者类当中。

4)使得类层次结构不改变的情况下，可以针对各个层次做出不同的操作，而不影响类层次结构的完整性。

5)可以跨越类层次结构，访问不同层次的元素类，做出相应的操作。
6)如果操作的逻辑改变，我们只需要改变访问者的实现就够了，而不用去修改其他所有的商品类。

7)添加新类别的商品到系统变得容易。只需要改变一下访问者接口以及其实现。已经存在的商品类别不会被干扰影响。



5。访问者模式缺点
1)增加新的元素会非常困难。

2)实现起来比较复杂，会增加系统的复杂性。

3)破坏封装，如果将访问行为放在各个元素中，则可以不暴露元素的内部结构和状态，但使用访问者模式的时候，为了让访问者能获取到所关心的信息，元素类不得不暴露出一些内部的状态和结构，就像收入和支出类必须提供访问金额和单子的项目的方法一样。

4)visit()方法的返回值的类型在设计系统式就需要明确。不然，就需要修改访问者的接口以及所有接口实现。另外如果访问者接口的实现太多，系统的扩展性就会下降。

"""


class Finance:
    def __init__(self):
        self.salesvolume = None  # 销售额
        self.cost = None  # 成本
        self.history_salesvolume = None  # 历史销售额
        self.history_cost = None  # 历史成本

    def set_salesvolume(self, value):
        self.salesvolume = value

    def set_cost(self, value):
        self.cost = value

    def set_history_salesvolume(self, value):
        self.history_salesvolume = value

    def set_history_cost(self, value):
        self.history_cost = value

    def accept(self, visitor):
        pass


# 2018年的财务情况
class Finance_year(Finance):
    def __init__(self, year):
        Finance.__init__(self)
        self.analyst = []
        self.year = year

    def add_analyst(self, worker):  # 有哪些分析师来分析数据
        self.analyst.append(worker)

    def accept(self):  # 分析师列表里面的人去分析数据
        for v in self.analyst:
            v.visit(self)


# 会计
class Accounting:
    def __init__(self):
        self.id = '会计'
        self.Duty = '计算报表'

    def visit(self, year_data):
        print('我现在分析的是{}年的数据'.format(year_data.year))
        print('我的身份是:{}，职责：'.format(self.id, self.Duty))
        print('本年度纯利润:{}'.format(year_data.salesvolume - year_data.cost))
        print('---------------------------------------')


# 财务总监
class Audit:
    def __init__(self):
        self.id = '财务总监'
        self.Duty = '分析业绩'

    def visit(self, year_data):  # 要把具体哪一年的数据传给分析师，让分析师去分析
        print('我现在分析的是{}年的数据'.format(year_data.year))
        print('我的身份是:{}，职责：'.format(self.id, self.Duty))
        if year_data.salesvolume - year_data.cost > year_data.history_salesvolume - year_data.history_cost:
            msg = '较同期上涨'
        else:
            msg = '较同期下跌'
        print('本年度公司业绩:{}'.format(msg))
        print('---------------------------------')


# 战略顾问
class Advisor:
    def __init__(self):
        self.id = '战略顾问'
        self.Duty = '制定明年策略'

    def visit(self, year_data):
        print('我现在分析的是{}年的数据'.format(year_data.year))
        print('我的身份是:{}，职责：'.format(self.id, self.Duty))
        if year_data.salesvolume > year_data.history_salesvolume:
            msg = '行业上涨，扩大规模'
        else:
            msg = '行业下跌，减少规模'
        print('本年度公司业绩:{}'.format(msg))
        print('------------------------------')


# 执行分析
class AnalyseData:
    def __init__(self):
        self.datalist = []  # 需要处理的数据列表,

    def add_data(self, year_data):
        self.datalist.append(year_data)

    def remove_data(self, year_data):
        self.datalist.remove(year_data)

    def visit(self):
        for d in self.datalist:
            d.accept()


if __name__ == '__main__':
    w = AnalyseData()  # 计划安排财务，总监，顾问对2018年数据处理
    finance_2018 = Finance_year(2018)  # 2018年的财务数据
    finance_2018.set_salesvolume(200)
    finance_2018.set_cost(90)
    finance_2018.set_history_salesvolume(190)
    finance_2018.set_history_cost(80)

    accounting = Accounting()
    audit = Audit()
    advisor = Advisor()

    finance_2018.add_analyst(accounting)  # 会计参与2018年的数据分析，然后执行了自己的visit方法
    finance_2018.add_analyst(audit)
    finance_2018.add_analyst(advisor)

    # finance_2018.accept()   #也可以直接这样调用
    w.add_data(finance_2018)
    w.visit()