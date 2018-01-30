# coding=utf-8

"""Remove Duplicates from Sorted Array II.

>>> solve = _solve1
>>> solve([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 4, 5, 6, 6, 7, 7, 7])
13
"""


def _solve(nums):
    if len(nums) < 3:
        return len(nums)
    new_len = 2
    for i in xrange(2, len(nums)):
        if nums[i] == nums[new_len - 1] == nums[new_len - 2]:
            continue
        else:
            nums[new_len] = nums[i]
            new_len += 1
    return new_len


# 因为数组有序，所以可以进一步优化下判断
def _solve1(nums):
    if len(nums) < 3:
        return len(nums)
    new_len = 2
    for i in xrange(2, len(nums)):
        if nums[i] != nums[new_len - 2]:
            nums[new_len] = nums[i]
            new_len += 1
    return new_len
