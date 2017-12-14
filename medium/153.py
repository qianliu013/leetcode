# coding=utf-8

"""Find Minimum in Rotated Sorted Array.

>>> solve = _solve
"""


def _solve(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] < nums[right]:
            return nums[left]
        mid = (left + right) / 2
        if nums[mid] < nums[right]:
            right = mid
        else:
            left = mid + 1
    return nums[left]
