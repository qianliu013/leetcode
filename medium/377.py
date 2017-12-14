# coding=utf-8

"""Combination Sum IV.

>>> solve = _solve
>>> _solve([1, 4, 3], 40)
119814916
"""


def _solve(nums, target):
    res = [1] + [0] * target
    for cur in xrange(1, target + 1):
        res[cur] += sum([res[cur - num] for num in nums if cur >= num])
    return res[target]
