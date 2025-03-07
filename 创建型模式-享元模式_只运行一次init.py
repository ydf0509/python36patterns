"""
相比这个文件，  创建型模式-享元模式.py

使 __init__ 只运行异常，阻止相同对象多次运行 __init__
"""

import dataset


class DatasetSink:
    # 类级别的实例缓存，按 db_url 存储
    _instances = {}
    _has__init_set =set()  # 把执行了 __init__的对象id保存起来对比

    def __new__(cls, db_url):
        # 如果 db_url 已存在，直接返回已有实例
        if db_url not in cls._instances:
            # 创建新实例并存入缓存
            self = super(DatasetSink, cls).__new__(cls)
            cls._instances[db_url] = self
        return cls._instances[db_url]

    def __init__(self, db_url):  # 相同的db_url不要每次都运行这个__init__。
        if id(self) not in self.__class__._has__init_set :
            print(f'创建连接 {db_url}')
            self.db = dataset.connect(db_url,ensure_schema=True)
            self.__class__._has__init_set.add(id(self))

    def save(self,  table_name:str,data:dict,):
        # 使用已有的连接插入数据
        table = self.db[table_name]
        table.insert(data)