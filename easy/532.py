# coding=utf-8

"""K-diff Pairs in an Array."""

from __future__ import print_function


# 因为 HashMap 为 O(n)，而排序为 O(n* log n)，所以其实 HashMap 可能会快一点？
def _solve(nums, k):
    if len(nums) < 2 or k < 0:
        return 0
    sorted_nums = sorted(nums)
    first, second = 0, 1
    prev, ans = -1, 0
    while second < len(nums):
        diff = sorted_nums[second] - sorted_nums[first]
        if diff < k:
            second += 1
        if diff > k:
            first += 1
            if first == second:
                second += 1
        if diff == k:
            if prev == -1 or sorted_nums[prev] != sorted_nums[first]:
                ans += 1
                prev = first
            second += 1
            first += 1
    return ans


if __name__ == '__main__':
    print (_solve([1, 1, 1], 0))
    print (_solve([3, 5, 3, 1, 1], 2))
    print (_solve([3, 1, 4, 1, 5], 2))
    print (_solve([1, 2, 3, 4, 5], 1))
    print (_solve([1, 3, 1, 5, 4], 0))
    print (_solve([3, 5, 3, 1, 1], 12))
