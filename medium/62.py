# coding=utf-8

"""Unique Paths

>>> solve = _solve
>>> solve(13, 13)
2704156
"""

import math


def _solve(m, n):
    dp = [1] * m
    for i in xrange(1, n):
        for j in xrange(1, m):
            dp[j] += dp[j - 1]
    return dp[-1]


# 可以视为数学问题
def _solve1(m, n):
    # return math.factorial(m + n - 2) / math.factorial(m - 1) / math.factorial(n - 1)
    res = 1
    for i in xrange(1, n):
        res = res * (m + i - 1) / i
    return res
