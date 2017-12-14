# coding=utf-8

"""Delete and Earn.

>>> solve = _solve
>>> solve([1, 1, 1, 2, 4, 5, 5, 5, 6])
18
"""

import collections


def _solve(nums):
    dp = [0] * 10001
    for num in nums:
        dp[num] += num
    for i in xrange(1, 10001):
        dp[i] = max(dp[i - 1], dp[i] + dp[i - 2])
    return dp[-1]


# 另一种比较简单的写法
def _solve1(nums):
    counter, prev, cur = collections.Counter(nums), 0, 0
    for value in range(10001):
        prev, cur = cur, max(prev + value * counter[value], cur)
    return cur
