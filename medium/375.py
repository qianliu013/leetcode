# coding=utf-8
"""Guess Number Higher or Lower II.

>>> solve = _solve2
>>> [solve(i) for i in xrange(10)]
[0, 0, 1, 2, 4, 6, 8, 10, 12, 14]
"""

import collections


# 只要尝试算一下 n 的前几个值，知道怎么算，dp 就能写出来
def _solve(n):
    dp = [[0] * (n + 2) for _ in xrange(n + 2)]
    for high in xrange(1, n + 1):
        for low in xrange(high - 1, 0, -1):
            # dp[low][high] = min(max(dp[low][mid - 1], dp[mid + 1][high]) + mid for mid in xrange(low, high + 1))
            dp[low][high] = min(
                max(dp[low][mid - 1], dp[mid + 1][high]) + mid for mid in xrange((low + high) / 2, high + 1))
    return dp[1][n]


# 这道题记忆化搜索要更快一点
def _solve1(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    def _dfs(low, high):
        if low >= high:
            return 0
        if dp[low][high]:
            return dp[low][high]
        dp[low][high] = min(
            mid + max(_dfs(low, mid - 1), _dfs(mid + 1, high)) for mid in xrange((low + high) / 2, high + 1))
        return dp[low][high]

    return _dfs(1, n)


# 此题其实存在 O(n^2) 的解法，具体解释可参考：
# https://artofproblemsolving.com/community/c296841h1273742
def _solve2(n):
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    for b in xrange(2, n + 1):
        k0 = b - 1
        deque = collections.deque()
        for a in xrange(b - 1, 0, -1):
            while dp[a][k0 - 1] > dp[k0 + 1][b]:
                if deque and deque[0][1] == k0:
                    deque.popleft()
                k0 -= 1
            vn = a + dp[a + 1][b]
            while deque and vn < deque[-1][0]:
                deque.pop()
            deque.append((vn, a))
            u1, u2 = dp[a][k0] + k0 + 1, deque[0][0]
            dp[a][b] = min(u1, u2)
    return dp[1][n]
