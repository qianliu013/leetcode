# coding=utf-8

"""Single Element in a Sorted Array.

>>> solve = _solve
>>> solve([1,1,2,3,3,4,4,8,8])
2
>>> solve([3,3,7,7,10,11,11])
10
"""


def _solve(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        if mid & 1:
            if nums[mid - 1] == nums[mid]:
                left = mid + 1
            else:
                right = mid - 2
        else:
            if nums[mid + 1] == nums[mid]:
                left = mid + 2
            else:
                right = mid - 1
    return nums[left]


# 简化版
def _solve1(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) >> 1
        mid = mid - (mid & 1)
        if nums[mid + 1] == nums[mid]:
            left = mid + 2
        else:
            right = mid - 1
    return nums[left]


def _solve2(nums):
    left, right = 0, len(nums) / 2
    while left < right:
        mid = (left + right) >> 1
        if nums[2 * mid] == nums[2 * mid + 1]:
            left = mid + 1
        else:
            right = mid
    return nums[2 * left]
