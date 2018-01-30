# coding=utf-8

"""Largest Number At Least Twice of Others.

>>> solve = _solve1
>>> solve([1])
0
>>> solve([3, 6, 1, 0])
1
>>> solve(range(4))
-1
"""


def _solve(nums):
    max_num = max(nums)
    if all(max_num >= 2 * x for x in nums if x != max_num):
        return nums.index(max_num)
    return -1


def _solve1(nums):
    max1, max2, idx = 0, 0, 0  # 0 <= nums[i] <= 99
    for i, num in enumerate(nums):
        if max1 < num:
            max1, max2, idx = num, max1, i
        elif max2 < num:
            max2 = num
    return idx if max1 >= 2 * max2 else -1
