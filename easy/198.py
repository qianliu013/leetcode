# coding=utf-8

"""House Robber."""

from __future__ import print_function


def _solve(nums):
    if not nums:
        return 0
    dp = [0 for _ in nums]
    for i, val in enumerate(nums):
        dp[i] = max(dp[i - 1] if i > 0 else 0,
                    (dp[i - 2] if i > 1 else 0) + nums[i])
    return dp[-1]


# 简化版
def _solve1(nums):
    last = now = 0
    for num in nums:
        last, now = now, max(now, last + num)
    return now


if __name__ == '__main__':
    print (_solve1([]))
    print (_solve1([1]))
    print (_solve1([2, 6, 3, 2, 2]))
