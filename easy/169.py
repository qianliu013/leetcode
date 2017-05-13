# coding=utf-8

"""Majority Element."""

from __future__ import print_function


def _majority_element(nums):
    result = {}
    majority = len(nums) / 2.0
    for num in nums:
        result[num] = result.get(num, 0) + 1
        if result[num] >= majority:
            return num


def _solve(nums):
    count = 0
    ans = 0
    for num in nums:
        if not count:
            ans = num
            count = 1
        elif num == ans:
            count += 1
        else:
            count -= 1
    return ans


if __name__ == '__main__':
    print (_majority_element([1, 1, 2, 3]))
    print (_solve([1, 1, 2, 3]))
