# coding=utf-8

"""Predict the Winner.

>>> solve = _solve1
>>> solve([1, 3, 1])
False
>>> solve([1, 5, 2])
False
>>> solve([1, 5, 233, 7]
True
"""


def _solve(nums):
    memo = {(i, i): num for i, num in enumerate(nums)}

    def _dfs(start, end, cur_sum):
        if (start, end) not in memo:
            memo[(start, end)] = cur_sum - min(_dfs(start, end - 1, cur_sum - nums[end]),
                                               _dfs(start + 1, end, cur_sum - nums[start]))
        return memo[(start, end)]

    return _dfs(0, len(nums) - 1, sum(nums)) * 2 >= sum(nums)


# 上述代码中一个优化是：其实无需知道最终的 sum，只要知道差值就可以，即改为
# memo[(start, end)] = max(nums[end] - _dfs(start, end - 1), nums[start] - _dfs(start + 1, end))
# 下面，根据这个优化，可以得出一种 dp 方法
# 不使用这个优化也可以得到，但是需要额外的处理，如计算前缀和或者计算两步前的最优值

def _solve1(nums):
    dp = [[0] * len(nums) for _ in xrange(len(nums) + 1)]
    for start in xrange(len(nums), -1, -1):
        for end in xrange(start + 1, len(nums)):
            dp[start][end] = max(nums[start] - dp[start + 1][end], nums[end] - dp[start][end - 1])
    return dp[0][-1] >= 0


# 空间 n^2 => n 优化
def _solve2(nums):
    dp = [0] * len(nums)
    for start in xrange(len(nums), -1, -1):
        for end in xrange(start + 1, len(nums)):
            dp[end] = max(nums[start] - dp[end], nums[end] - dp[end - 1])
    return dp[-1] >= 0


# 最后 n 为偶数是必胜的
