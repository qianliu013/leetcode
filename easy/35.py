# coding=utf-8

"""Search Insert Position."""

from __future__ import print_function


def _solve(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


def _solve1(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # 或者改为
    # right = mid
    # return mid
    return left + (1 if nums[left] < target else 0)


if __name__ == '__main__':
    NUMBERS = [1, 3, 5, 6]
    print (_solve1(NUMBERS, 5))
    print (_solve1(NUMBERS, 2))
    print (_solve1(NUMBERS, 7))
    print (_solve1(NUMBERS, 0))
    NUMBERS1 = [1, 3]
    print (_solve1(NUMBERS1, 0))
    print (_solve1(NUMBERS1, 2))
    print (_solve1(NUMBERS1, 4))
