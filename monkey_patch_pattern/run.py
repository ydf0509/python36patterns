# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 12:12
"""重要程度 ☆☆☆☆
利用模块只会导入一次，模块天然单例的特性，使用猴子补丁。一处修改 处处生效。
猴子补丁是python动态语言的重要设计模式，能用很少代码，大幅度改变很多地方的运行行为。
对多人合作的大项目，如果猴子补丁直接在__init__.py里面执行了，并且猴子补丁变化有很大影响，则需要告诉小伙伴，免得出现莫名其妙的疑惑。
"""
from monkey_patch_pattern import a


from  monkey_patch_pattern.b import funbbb  # TODO 请注释掉该行，测试在一开头导入funbbb和在打了猴子补丁之后再导入funbbb

def modify_fun():
    print('修改后的 print world')


a.fun = modify_fun

a.fun()

print('- - - - - ')
# from monkey_patch_pattern.b import funbbb   # TODO 请注释掉该行，请测试在一开头导入funbbb和在打了猴子补丁之后再导入funbbb

funbbb()

"""
如果在第19行，即打了猴子补丁后再导入funbbb，结果是：
修改后的 print world
- - - - - 
funbbbb中调用fun
修改后的 print world



如果在开头行，即在打猴子补丁之前导入funbbb，结果是：
修改后的 print world
- - - - - 
funbbbb中调用fun
原始的 print hello

"""