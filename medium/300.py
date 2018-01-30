# coding=utf-8

"""Longest Increasing Subsequence.

>>> solve = _solve1
>>> solve([10, 9, 2, 5, 3, 7, 101, 18])
4
"""

import bisect


# O(n ^ 2)
def _solve(nums):
    dp = [1] * len(nums) + [0]
    for i, cur in enumerate(nums):
        for j, prev in enumerate(nums[:i]):
            if prev < cur:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# O(n * log(n))
def _solve1(nums):
    if not nums:
        return 0
    dp = [nums[0]]
    for num in nums[1:]:
        if num > dp[-1]:
            dp.append(num)
        elif num < dp[0]:
            dp[0] = num
        else:
            dp[bisect.bisect_left(dp, num)] = num
    return len(dp)
