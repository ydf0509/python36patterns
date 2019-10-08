# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/8 0008 16:41
"""
重要的模式之一。使用这种模式可以创造数据库连接池 浏览器池等。
实现原理有两个重要的地方是，使用时候借，使用完成后归还。我使用这个创造了一个非常强大的场景。
最好是使用with语法来完成对象的借和还，减少调用处的代码。

资源受限的, 不需要可伸缩性的环境(cpu\内存等物理资源有限): cpu性能不够强劲, 内存比较紧张, 垃圾收集, 内存抖动会造成比较大的影响, 需要提高内存管理效率, 响应性比吞吐量更为重要;
数量受限的, 比如数据库连接;
创建成本高的对象, 可以考虑是否池化, 比较常见的有线程池（ThreadPoolExecutor）, 字节数组池等。
"""
from queue import Queue
from monkey_print2 import print


class QueueObject():

    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.object = self._queue.get() if auto_get else None

    def __enter__(self):
        if self.object is None:
            self.object = self._queue.get()
        return self.object

    def __exit__(self, Type, value, traceback):
        if self.object is not None:
            self._queue.put(self.object)
            self.object = None

    def __del__(self):
        if self.object is not None:
            self._queue.put(self.object)
            self.object = None


def main():
    sample_queue = Queue()
    sample_queue.put('yam')
    with QueueObject(sample_queue) as obj:
        print('Inside with: {}'.format(obj))
    print('Outside with: {}'.format(sample_queue.get()))

    sample_queue.put('sam')
    queue_object = QueueObject(sample_queue, True)
    print('内部 func: {}'.format(queue_object.object))
    print('外部 func: {}'.format(sample_queue.get()))

    if not sample_queue.empty():
        print(sample_queue.get())


if __name__ == '__main__':
    main()
