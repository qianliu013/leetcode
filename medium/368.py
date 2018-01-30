# coding=utf-8
"""Largest Divisible Subset.

>>> solve = _solve1
>>> sorted(solve([3, 4, 6, 8, 12, 16, 32]))
[4, 8, 16, 32]
"""


# 只要想清楚最终结果中数满足的特点就很容易想出 dp 方法
def _solve(nums):
    nums.sort(reverse=True)
    length = len(nums)
    dp = [[] for _ in nums]
    ans = []
    for i in xrange(length):
        for j in xrange(i):
            if nums[j] % nums[i] == 0 and len(dp[i]) < len(dp[j]):
                dp[i] = list(dp[j])
        dp[i].append(nums[i])
        if len(dp[i]) > len(ans):
            ans = dp[i]
    return ans


# 此为上面代码思想的一种简洁的写法（只有四行）
# https://discuss.leetcode.com/topic/49455/4-lines-in-python


# 上述代码中复制了 dp[j]；虽然 dp[j] 的长度不可能高，不过依旧可以优化这一点
def _solve1(nums):
    nums.sort()
    length = len(nums)
    prev, count = [0] * length, [0] * length
    res = [-1, 0]

    for i in xrange(length):
        prev[i], count[i] = -1, 1
        for j in xrange(i):
            if nums[i] % nums[j] == 0 and count[j] + 1 > count[i]:
                prev[i] = j
                count[i] = count[j] + 1
        if count[i] > res[1]:
            res = [i, count[i]]
    ans = []
    while res[0] != -1:
        ans.append(nums[res[0]])
        res[0] = prev[res[0]]
    return ans
