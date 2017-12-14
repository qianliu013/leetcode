# coding=utf-8

"""Unique Binary Search Trees.

>>> solve = _solve
>>> solve(9)
4862
"""


# 此题结果是著名的卡塔兰数，可以应用到很多问题上，具体可参考
# http://en.wikipedia.org/wiki/Catalan_number
import math


def _solve(n):
    dp = [1] * (n + 1)
    for i in xrange(2, n + 1):
        dp[i] = sum([dp[j] * dp[i - 1 - j] for j in xrange(i)])
    return dp[-1]


def _solve1(n):
    # res = 1
    # for i in xrange(n + 1, 2 * n + 1):
    #     res = res * i / (i - n)
    # return res / (n + 1)
    return math.factorial(2 * n) / math.factorial(n) / math.factorial(n + 1)
