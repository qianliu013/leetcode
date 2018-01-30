# coding=utf-8

"""Increasing Triplet Subsequence.

>>> solve = _solve
>>> solve([1, 2, 2, 1])
False
>>> solve([1, 1, -2, 6])
False
>>> solve([1, 1, 2, 1, 2, 3])
True
"""


def _solve(nums):
    small, mid = float('inf'), float('inf')
    for num in nums:
        if num <= small:
            small = num
        elif num <= mid:
            mid = num
        else:
            return True
    return False
