# coding=utf-8

"""Minimum Path Sum.

>>> solve = _solve
>>> solve([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
7
"""


def _solve(grid):
    height, width = len(grid), len(grid[0])
    dp = [0] * width
    for i in xrange(width):
        dp[i] = dp[i - 1] + grid[0][i]
    for i in xrange(1, height):
        dp[0] += grid[i][0]
        for j in xrange(1, width):
            dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
    return dp[-1]
