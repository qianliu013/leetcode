# coding=utf-8

"""Target Sum.

>>> solve = _solve2
>>> solve([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 3)
330
"""

import collections


def _solve(nums, S):
    res = {0: 1}
    for num in nums:
        tmp = collections.defaultdict(int)
        for cur, count in res.items():
            tmp[cur + num] += count
            tmp[cur - num] += count
        res = tmp
    return res[S]


def _solve1(nums, S):
    num_sum = sum(nums)
    if S > num_sum or S < -num_sum:
        return 0
    dp = [0] * (2 * num_sum + 1)
    dp[0 + num_sum] = 1
    for num in nums:
        tmp = [0] * (2 * num_sum + 1)
        for i in xrange(2 * num_sum + 1):
            if dp[i] > 0:
                tmp[i + num] += dp[i]
                tmp[i - num] += dp[i]
        dp = tmp
    return dp[num_sum + S]


# 参考自 https://discuss.leetcode.com/topic/76243/java-15-ms-c-3-ms-o-ns-iterative-dp-solution-using-subset-sum-with-explanation
def _solve2(nums, S):
    num_sum = sum(nums)
    if S > num_sum or S < -num_sum or (S + num_sum) % 2 > 0:
        return 0
    half = (S + num_sum) / 2
    dp = [1] + [0] * half
    for num in nums:
        for i in xrange(half, num - 1, -1):
            dp[i] += dp[i - num]
    return dp[half]
