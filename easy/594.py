# coding=utf-8

"""Longest Harmonious Subsequence."""

from __future__ import print_function
import collections


def _solve(nums):
    result = collections.defaultdict(int)
    result_reduce1 = collections.defaultdict(int)
    for num in nums:
        result[num] += 1
        result_reduce1[num - 1] += 1
    ans = 0
    for num in result:
        if num in result_reduce1:
            ans = max(ans, result[num] + result_reduce1[num])
    return ans


def _solve1(nums):
    if not nums:
        return 0
    sorted_nums = sorted(nums)
    ans, length = 0, len(nums)
    i_left, i_mid, i_right = 0, 0, 0
    while i_mid < length and sorted_nums[i_left] == sorted_nums[i_mid]:
        i_mid += 1
    while i_right < length:
        i_right = i_mid
        while i_right < length and sorted_nums[i_mid] == sorted_nums[i_right]:
            i_right += 1
        if sorted_nums[i_right - 1] - 1 == sorted_nums[i_left]:
            ans = max(i_right - i_left, ans)
        i_left, i_mid = i_mid, i_right
    return ans


def _solve2(nums):
    result = {}
    ans = 0
    for num in nums:
        result[num] = result.get(num, 0) + 1
        if num - 1 in result:
            ans = max(ans, result[num] + result[num - 1])
        if num + 1 in result:
            ans = max(ans, result[num] + result[num + 1])
    return ans


if __name__ == '__main__':
    NUMS = [1, 3, 2, 2, 5, 2, 3, 7]
    print (_solve2(NUMS))
    print (_solve2([]))
    print (_solve2([1, 1]))
    print (_solve2([1, 1, 2, 2]))
    print (_solve2([1, 1, 2, 2, 3, 3]))
    print (_solve2([1, 2, 4, 5, 5]))
