# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 10:39

"""重要程度 ☆☆☆
订阅-发布模式和观察者模式概念相似，但在订阅-发布模式中，订阅者和发布者之间多了一层中间件：一个被抽象出来的信息调度中心。

但其实没有必要太深究 2 者区别，因为《Head First 设计模式》这本经典书都写了：发布+订阅=观察者模式。其核心思想是状态改变和发布通知。在此基础上，根据语言特性，进行实现即可。

对比观察者模式看。23种经典设计模式里面不包括发布订阅设计模式，区别太小。
"""

class Event:
    def __init__(self):
        self.client_list = {}

    def listen(self, key, fn):
        if key not in self.client_list:
            self.client_list[key] = []
        self.client_list[key].append(fn)

    def trigger(self, *args, **kwargs):
        fns = self.client_list[args[0]]

        length = len(fns)
        if not fns or length == 0:
            return False

        for fn in fns:
            fn(*args[1:], **kwargs)

        return False

    def remove(self, key, fn):
        if key not in self.client_list or not fn:
            return False

        fns = self.client_list[key]
        length = len(fns)

        for _fn in fns:
            if _fn == fn:
                fns.remove(_fn)

        return True


# 借助继承为对象安装 发布-订阅 功能
class SalesOffice(Event):
    def __init__(self):
        super().__init__()


# 根据自己需求定义一个函数：供事件处理完后调用
def handle_event(event_name):
    def _handle_event(*args, **kwargs):
        print("Price is", *args, "at", event_name)

    return _handle_event


if __name__ == "__main__":
    # 创建2个回调函数
    fn1 = handle_event("event01")
    fn2 = handle_event("event02")

    sales_office = SalesOffice()

    # 订阅event01 和 event02 这2个事件，并且绑定相关的 完成后的函数
    sales_office.listen("event01", fn1)
    sales_office.listen("event02", fn2)

    # 当两个事件完成时候，触发前几行绑定的相关函数
    sales_office.trigger("event01", 1000)
    sales_office.trigger("event02", 2000)

    sales_office.remove("event01", fn1)

    # 打印：False
    print(sales_office.trigger("event01", 1000))
