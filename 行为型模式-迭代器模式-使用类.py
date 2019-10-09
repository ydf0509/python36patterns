# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 11:49

class AccountIterator():
    def __init__(self, accounts):
        self.accounts = accounts  # 账户集合
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.accounts):
            raise StopIteration("到头了...")
        else:
            self.index += 1
            return self.accounts[self.index - 1]


if __name__ == '__main__':
    account_iter = AccountIterator(['a','b','c','d'])
    print(next(account_iter))
    print('----')
    for a in account_iter:
        print(a)
