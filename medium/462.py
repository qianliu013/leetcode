# coding=utf-8

"""Minimum Moves to Equal Array Elements II.

>>> solve = _solve1
>>> solve([1,2,3])
2
>>> solve([1,1,100])
99
"""

import random


def _solve(nums):
    if not nums:
        return 0
    median = sorted(nums)[len(nums) / 2]
    return sum(abs(num - median) for num in nums)


def _solve1(nums):
    nums.sort()
    return sum(nums[~i] - nums[i] for i in xrange(len(nums) / 2))


def _solve2(nums):
    def _nth(nums, nth, start, end):
        left, right, pivot = start, end, nums[start]
        while True:
            while left < right and nums[right] > pivot:
                right -= 1
            while left < right and nums[left] <= pivot:
                left += 1
            if left >= right:
                break
            nums[left], nums[right] = nums[right], nums[left]
        nums[start], nums[right] = nums[right], nums[start]
        if nth == left:
            return pivot
        elif nth < left:
            return _nth(nums, nth, start, left - 1)
        else:
            return _nth(nums, nth, left + 1, end)
    # 如果不使用 shuffle，遇到有序大数组将导致 maximum recursion depth exceeded 或超时
    random.shuffle(nums)
    median = _nth(nums, len(nums) / 2, 0, len(nums) - 1)
    return sum(abs(num - median) for num in nums)


# 上述写法，如果交换 while 中的两个 while 顺序，那么结果是错的
# 如果交换顺序，如下述做法，进行 -1 补偿，依旧是错的
# def _nth1(nums, nth, start, end):
#     left, right, pivot = start, end, nums[start]
#     while True:
#         while left < right and nums[left] <= pivot:
#             left += 1
#         while left < right and nums[right] > pivot:
#             right -= 1
#         if left >= right:
#             break
#         nums[left], nums[right] = nums[right], nums[left]
#     nums[start], nums[right - 1] = nums[right - 1], nums[start]
#     if nth == left - 1:
#         return pivot
#     elif nth < left - 1:
#         return _nth1(nums, nth, start, left - 2)
#     else:
#         return _nth1(nums, nth, left, end)
