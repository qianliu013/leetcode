# coding=utf-8

"""Bulb Switcher II.

>>> solve = _solve
>>> solve()

"""


def _solve(n, m):
    if m == 0 or n == 0:
        return 1
    if n == 1:
        return 2
    if n == 2:
        return 3 if m == 1 else 4
    if m == 1:
        return 4
    return 7 if m == 2 else 8


# 另一种方法是计算状态的所有的可能性：有效操作类型最多 16 种，而 n > 3 可以用 3 来代表
# 所以计算量不大，具体写法可参考
# https://discuss.leetcode.com/topic/102077/python-straightforward-with-explanation
