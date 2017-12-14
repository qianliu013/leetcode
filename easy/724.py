# coding=utf-8

"""Find Pivot Index.

>>> solve = _solve
>>> solve([1, -1])
-1
>>> solve([0, 1, -1])
0
>>> solve([1, -1, 0])
2
"""


def _solve(nums):
    prev, sum_num = 0, sum(nums)
    for i, num in enumerate(nums):
        if prev * 2 + num == sum_num:
            return i
        prev += num
    return -1
