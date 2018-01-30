# coding=utf-8

"""Ones and Zeroes.

>>> solve = _solve
>>> solve(["10", "0001", "111001", "1", "0"], 3, 4)
3
"""

import collections


# python 使用 dict 来完成 dp 的方法通常要快于正常的 dp 写法
def _solve(strs, m, n):
    pairs = []
    for s in strs:
        tmp = [0, 0]
        for ch in s:
            tmp[ord(ch) - 48] += 1
        pairs.append(tmp)
    res = collections.defaultdict(int)
    res[(0, 0)] = 0
    for c0, c1 in pairs:
        for (count0, count1), max_num in res.items():
            if count0 + c0 <= m and count1 + c1 <= n:
                res[(count0 + c0, count1 + c1)] = max(max_num + 1, res[(count0 + c0, count1 + c1)])
    return max(res.values())


# 正常的 dp 写法
def _solve1(strs, m, n):
    dp = [[0] * (n + 1) for _ in xrange(m + 1)]
    for s in strs:
        counter = [0, 0]
        for ch in s:
            counter[ord(ch) - 48] += 1
        for i in xrange(m, counter[0] - 1, -1):
            for j in xrange(n, counter[1] - 1, -1):
                dp[i][j] = max(dp[i][j], dp[i - counter[0]][j - counter[1]] + 1)
    return dp[m][n]
