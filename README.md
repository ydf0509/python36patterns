```
编程时候，设计新的模块或者项目，下不了笔，要思考三天三夜怎么设计，主要是没学设计模式。

编程时候，有时候脑子一瞬间感觉 灵光出现，觉得这么写台好了太合适了，这样写节约代码 扩展高，瞬间感到这是个天才想法，
主要是由于没有专门学习设计模式，只能偶尔灵机一动，形成不了一套稳定的输出，所以才会有这种突然感觉某个代码设计是天才设计这种感受。
```

```
不要纠结是23种还是36种了，有细分的，举个例子 观察者模式和发布订阅模式，是有了少许变化，多了解一种总没啥坏处。
为什么是36种，因为是摘自菜鸟教程或者w3cschool网站，这两个网站都是36种，包含了j2ee模式，多了解没坏处。
不愿意学oop和设计模式，天天加班写bug解bug无限复制粘贴扣字老代码写新代码，这种写法瞎忙也没用。
比如韩信3万军队歼灭70万大军，靠的不是大无畏的胡乱冲刺，而是因为韩信看了孙子兵法36计兵书，靠的是策略，所以我要称之为36种设计模式。

设计模式十分有用，是通过大量实践对比得出来的，比如和自己国王写代码的纵向对比总结，和公司n多个现有代码项目的横向对比总结得出来的结论。

使用设计模式或oop转化公式，能使几乎任意项目代码减少50%至90%行，编码速度快一倍。
扩展性和维护性提高数十倍，bug减少5倍。
如果是使用极端纯面向过程（或者加入了少量无效废物类）的方式来写python代码，
我不用看，就知道一定很low。
```


## 一些介绍
学弟啊，你代码能不能不要写得这么烂
https://www.toutiao.com/a6739759206997426696/

面向对象和面向过程分别是什么？
https://www.zhihu.com/question/28790424

如何通俗易懂地举例说明「面向对象」和「面向过程」有什么区别？
https://www.zhihu.com/question/27468564


对于程序员来说，设计模式和算法哪个更重要呢？
https://www.zhihu.com/question/25432487

为什么我们需要学习（设计）模式
https://zhuanlan.zhihu.com/p/19835717


## 介绍神级别通用固定oop转化公式，写代码下笔时候行云流水。

使用这个公式，不需要背设计模式，不需要每次写新文件先花几天想破头皮怎么设计布局代码成为高扩展和高维护。

## 常见问题回答

1、老是纠结类和函数？类和函数有什么区别。

```
问函数和类的区别，这简直是牛头不对马嘴的伪问题。
函数和方法可以比区别。函数和类比区别就是问 人和上班 、猪和吃东西 有什么区别一样，简直是没搞清楚比较维度。

类和模块可以比，类主要优势是多实例，多个实例的属性是互不干扰的，每个实例的多个方法都可以直接访问实例属性(成员变量)。
面向过程是一直很low的在函数间把本应该在oop中声明为成员变量的东西弄成在函数间反复传参和return。

类 + 方法 + 实例属性(成员变量)  约等于    模块 + 函数 + 全局变量
1）对于类，类的无数个实例化对象的实例属性(成员变量)是互不干扰的，天然的多实例。
2）对于模块 python的模块在当前解释器中是唯一的，import 一万次 xx.py，xx模块都是唯一的指向同一个地方，
所以使用全局变量 加 函数逇设计方式是行不通的，xx模块是唯一的，xx模块的a 变量 b变量也是惟一的，
所以老是需要设计成吧a和b弄成传参和return而不是全局变量来解决全局变量只有一份的问题。

所以如果需要多实例，类 + 方法 + 实例属性(成员变量) 远好于 模块 + 函数 + 全局变量。
模块 + 函数 + 全局变量 由于要模拟多实例，使全局变量（状态） 不唯一，大部分情况下需要写成 函数反复传参和反复return。
这种面向过程的封装的写法曲折程度毫无疑问被oop暴击了，面向过程导致写代码慢想破头皮搞一堆传参和return。何况oop不只有封装还有继承和多态。

能写类的人100%就能写函数，能写函数的人不一定能写类（说的是真oop的类，排除无效废物面向过程滑稽类），这是不可逆的。
```

2、 不学设计模式的坏处

```
只爱学python语法，只学怎么使用if else break， 学字典 列表怎么用，代码就很low
写代码很慢，设计慢，想的慢，打字慢
代码不可维护，没有高扩展性
写新文件要想破头皮三天三夜才能开始下笔。
```

## ！【重要】 简单例子说明极端面向过程编程非常愚蠢low

情不自禁纯粹极端面向过程编程还是c语言中毒了，从来都不使用面向对象，不用提设计模式。

有些人完全没思考过面向对象，一味的只会说大型项目才需要面向对象，小项目面向过程更合适。简直是胡说八道，不看场景只看项目大小。

比如一个简单需求，描写人,吃饭 增加体重和身高，拉尿体重降低。需求是非常非常的简单了吧，绝对是非常小的项目，单个文件就好了，来验证下是不是小项目面向过程最好。

面向过程来实现，看看代码实现多垃圾，调用时候多么麻烦。
```python
# 吃饭函数
def eat(name, height, weight, food_weight):
    """吃饭：增加体重和身高"""
    new_weight = weight + food_weight
    new_height = height + food_weight * 0.01
    print(f"{name} 吃了 {food_weight} 千克食物，体重: {new_weight} 千克，身高: {new_height} 厘米")
    return new_height, new_weight

# 拉尿函数
def pee(name, height, weight, pee_weight):
    """拉尿：减少体重"""
    if pee_weight > weight:
        pee_weight = weight
    new_weight = weight - pee_weight
    print(f"{name} 拉了 {pee_weight} 千克尿，体重: {new_weight} 千克，身高: {height} 厘米")
    return height, new_weight

# 测试代码
if __name__ == "__main__":
    # 小明的初始状态
    xiaoming_height = 170
    xiaoming_weight = 60

    # 小红的初始状态
    xiaohong_height = 160
    xiaohong_weight = 50

    print(f"小明 初始状态 - 身高: {xiaoming_height} 厘米，体重: {xiaoming_weight} 千克")
    print(f"小红 初始状态 - 身高: {xiaohong_height} 厘米，体重: {xiaohong_weight} 千克")

    # 小明吃饭和拉尿
    xiaoming_height, xiaoming_weight = eat("小明", xiaoming_height, xiaoming_weight, 2)
    xiaoming_height, xiaoming_weight = pee("小明", xiaoming_height, xiaoming_weight, 1)

    # 小红吃饭和拉尿
    xiaohong_height, xiaohong_weight = eat("小红", xiaohong_height, xiaohong_weight, 3)
    xiaohong_height, xiaohong_weight = pee("小红", xiaohong_height, xiaohong_weight, 2)
```

面向对象来实现，看看代码实现多简单调用多方便
```python
class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height  # 身高，单位：厘米
        self.weight = weight  # 体重，单位：千克

    def eat(self, food_weight):
        """吃饭：增加体重和身高"""
        self.weight += food_weight
        self.height += food_weight * 0.01
        print(f"{self.name} 吃了 {food_weight} 千克食物，体重: {self.weight} 千克，身高: {self.height} 厘米")

    def pee(self, pee_weight):
        """拉尿：减少体重"""
        if pee_weight > self.weight:
            pee_weight = self.weight
        self.weight -= pee_weight
        print(f"{self.name} 拉了 {pee_weight} 千克尿，体重: {self.weight} 千克，身高: {self.height} 厘米")

# 测试代码
if __name__ == "__main__":
    # 创建小明和小红
    xiaoming = Person("小明", 170, 60)
    xiaohong = Person("小红", 160, 50)

    # 小明吃饭和拉尿
    xiaoming.eat(2)
    xiaoming.pee(1)

    # 小红吃饭和拉尿
    xiaohong.eat(3)
    xiaohong.pee(2)
```

```
面向对象起码有封装，极端面向过程那就实现时候，每个函数结尾需要疯狂的return 一大堆变量，然后将一大堆变量传给另外一个函数进行处理。
而面向对象不需要你把一大堆入参疯狂在各个函数传来传去，return来return去。


如果你给我说，定义一个结构体或者字典来存放 身高 体重 姓名，然后充分利用字典是可变类型，这样既减少了每个函数的入参数量，
又不需要return一大堆变量，还是可以用面向过程来写这个代码，
就避免了上面我说的疯狂传参和疯狂return的弊端，那么继承和多态阁下有如何应对呢？ 

比如大人吃1kg长0.1kg体重，小孩吃1kg长0.2kg体重，并且我假设eat函数调用了另外一个_eat2的私有函数来执行体重增加计算，
你在面向过程时候，要加一个 大人eat的函数 加一个 大人_eat2 的函数，  并且大人eat的函数里面调用大人_eat2的函数，整个链路的就都要替换，
你想下纯粹极端面向过程实现公共代码时候有多low多复杂，并且调用它的时候有多麻烦。

如果你的思维是c语言中毒了，情不自禁极端面向过程编程，连入门的面向对象封装概念都没有，更别提更高阶的设计模式了。

```

#### 只需要按文档的面向过程转 oop 4步走里面的固定公式，全局变量->实例属性，函数->方法 降维转化，就可以设计出强大的代码，无需死记硬背23种设计模式。