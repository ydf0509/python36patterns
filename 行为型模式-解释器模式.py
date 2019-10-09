# -*- coding: utf-8 -*-
# @Author  : ydf
# @Time    : 2019/10/9 0009 9:35
"""
重要程度 ☆☆

解释器模式（Interpreter Pattern）提供了评估语言的语法或表达式的方式，它属于行为型模式。这种模式实现了一个表达式接口，该接口解释一个特定的上下文。这种模式被用在 SQL 解析、符号处理引擎等。

对每个应用来说，至少有以下两种不同的用户分类。
 基本用户：这类用户只希望能够凭直觉使用应用。他们不喜欢花太多时间配置或学习应
用的内部。对他们来说，基本的用法就足够了。
 高级用户：这些用户，实际上通常是少数，不介意花费额外的时间学习如何使用应用的
高级特性。如果知道学会之后能得到以下好处，他们甚至会去学习一种配置（或脚本）
语言。
 能够更好地控制一个应用
 以更好的方式表达想法
 提高生产力
解释器（Interpreter）模式仅能引起应用的高级用户的兴趣。这是因为解释器模式背后的主
要思想是让非初级用户和领域专家使用一门简单的语言来表达想法。然而，什么是一种简单的语
言？对于我们的需求来说，一种简单的语言就是没编程语言那么复杂的语言
"""
from monkey_print2 import print


class PlayContext():
    play_text = None


class Expression():
    def interpret(self, context):
        if len(context.play_text) == 0:
            return
        else:
            play_segs = context.play_text.split(" ")
            for play_seg in play_segs:
                pos = 0
                for ele in play_seg:
                    if ele.isalpha():
                        pos += 1
                        continue
                    break
                play_chord = play_seg[0:pos]
                play_value = play_seg[pos:]
                self.execute(play_chord, play_value)

    def execute(self, play_key, play_value):
        pass


class NormGuitar(Expression):
    def execute(self, key, value):
        print("Normal Guitar Playing--Chord:%s Play Tune:%s" % (key, value))


if __name__ == "__main__":
    context = PlayContext()
    context.play_text = "C53231323 Em43231323 F43231323 G63231323"
    guitar = NormGuitar()
    guitar.interpret(context)
    """
    "D:/coding2/python36patterns/行为型模式-解释器模式.py:29"  09:37:28  Normal Guitar Playing--Chord:C Play Tune:53231323
    "D:/coding2/python36patterns/行为型模式-解释器模式.py:29"  09:37:28  Normal Guitar Playing--Chord:Em Play Tune:43231323
    "D:/coding2/python36patterns/行为型模式-解释器模式.py:29"  09:37:28  Normal Guitar Playing--Chord:F Play Tune:43231323
    "D:/coding2/python36patterns/行为型模式-解释器模式.py:29"  09:37:28  Normal Guitar Playing--Chord:G Play Tune:63231323
    """
