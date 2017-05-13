# coding=utf-8

"""Contains Duplicate II."""

import collections


def _solve(nums, k):
    if k < 1:
        return False
    result = {}
    for index, num in enumerate(nums):
        if num in result and index - result[num] <= k:
            return True
        result[num] = index
    return False


def _solve1(nums, k):
    if k < 1:
        return False
    result = set()
    for index, num in enumerate(nums):
        if index > k:
            result.remove(nums[index - k - 1])
        if num in result:
            return True
        result.add(num)
    return False


if __name__ == '__main__':
    print _solve1([], 0)
    for diff in range(3):
        print _solve1([1, 2, 1, 2, 1], diff)
