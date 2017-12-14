# coding=utf-8

"""Contiguous Array.

>>> solve = _solve
>>> solve([0, 1])
2
"""


def _solve(nums):
    first, diff, ans = {0: -1}, 0, 0
    for i, num in enumerate(nums):
        diff += 1 if num else -1
        if diff in first:
            ans = max(ans, i - first[diff])
        else:
            first[diff] = i
    return ans
