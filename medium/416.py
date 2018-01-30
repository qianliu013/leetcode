# coding=utf-8

"""Partition Equal Subset Sum.

>>> solve = _solve
>>> solve([1, 5, 11, 5])
True
>>> solve([1, 2, 3, 5])
False
"""


def _solve(nums):
    sum_nums = sum(nums)
    if sum_nums & 1:
        return False
    half = sum_nums / 2
    dp = [True] + [False] * half
    for num in nums:
        for i in xrange(half, num - 1, -1):
            dp[i] |= dp[i - num]
    return dp[-1]


# 上述代码中的 dp 状态转移，是一个当前 sum 子集到下一个 sum 子集的转变
# 由于只需要考虑存在与否，此题数据数据不大，其实可以使用位运算极大优化这个过程
def _solve1(nums):
    sum_val, bits = 0, 1
    for num in nums:
        sum_val += num
        bits |= bits << num
    return (sum_val & 1 != 1) and (bits >> (sum_val / 2)) & 1 == 1
