# coding=utf-8

"""Degree of an Array.

>>> solve = _solve
>>> solve([1, 2, 2, 3, 1])
2
>>> solve([1, 2, 2, 3, 1, 4, 2])
6
"""


def _solve(nums):
    res, degree = {}, 1
    for i, num in enumerate(nums):
        if num in res:
            tmp = res[num]
            tmp[0] += 1
            tmp[2] = i
            degree = max(tmp[0], degree)
        else:
            res[num] = [1, i, i]
    return min([right - left for frequency, left, right in res.values() if frequency == degree]) + 1
