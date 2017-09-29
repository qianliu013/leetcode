# coding=utf-8

"""Longest Continuous Increasing Subsequence.

>>> solve = _solve
>>> solve([1, 3, 5, 4, 7])
3
>>> solve([2, 2, 2, 2])
1
"""


def _solve(nums):
    res, ans, prev = 0, 0, float('-inf')
    for num in nums:
        if num > prev:
            res += 1
        else:
            res = 1
        ans = max(ans, res)
        prev = num
    return ans
