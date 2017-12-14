# coding=utf-8

"""Subarray Sum Equals K.

>>> solve = _solve
>>> solve([2, 1, 1, 1, 2], 2)
4
"""


def _solve(nums, k):
    res, ans, prefix_sum = {0: 1}, 0, 0
    for num in nums:
        prefix_sum += num
        ans += res.get(prefix_sum - k, 0)
        res[prefix_sum] = res.get(prefix_sum, 0) + 1
    return ans
