# coding=utf-8

"""Maximum Product of Three Numbers.

>>> _solve([1,2,3])
6
>>> _solve([1,2,3,4])
24
"""


def _solve(nums):
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3], nums[-1] * nums[0] * nums[1])
