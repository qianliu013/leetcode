# coding=utf-8

"""Non-decreasing Array.

>>> solve = _solve
>>> solve([1, 2, 3])
True
>>> solve([4, 2, 3])
True
>>> solve([4, 2, 1])
False
>>> solve([3, 4, 2, 3])
False
>>> solve([2, 3, 3, 2, 4])
True
"""


# 注意边界下降两个端点的考虑
def _solve(nums):
    prev, count, break_index = nums[0], 0, 0
    for i, num in enumerate(nums[1:]):
        if num < prev:
            count += 1
            break_index = i + 1
        if count > 1:
            return False
        prev = num
    if count == 0:
        return True
    if break_index == len(nums) - 1 or nums[break_index - 1] <= nums[break_index + 1]:
        return True
    if break_index - 1 == 0 or nums[break_index - 2] <= nums[break_index]:
        return True
    return False
