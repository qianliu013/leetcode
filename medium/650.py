# coding=utf-8

"""2 Keys Keyboard.

>>> solve = _solve2
>>> [solve(i) for i in range(1, 20)]
[0, 2, 3, 4, 5, 5, 7, 6, 6, 7, 11, 7, 13, 9, 8, 8, 17, 8, 19]
"""

import math


def _solve(n):
    max_num = float('inf')
    res = [{} for _ in xrange(n + 1)]
    res[1][0], res[1][1] = 0, 1
    for length in xrange(1, n + 1):
        for paste, step in res[length].items():
            if length + paste <= n:
                res[length + paste][paste] = min(res[length + paste].get(paste, max_num), step + 1)
            if length * 2 <= n:
                res[length * 2][length] = min(res[length * 2].get(length, max_num), step + 2)
    return min(res[n].values())


# 上述方法在扩展时太暴力了，其实只需考虑当前 Length 最大的因子即可

def _solve1(n):
    dp = range(n + 1)
    dp[1] = 0
    for i in xrange(2, n + 1):
        for j in xrange(i / 2, 1, -1):
            if i % j == 0:
                dp[i] = dp[j] + (i / j)
                break
    return dp[n]


def _solve2(n):
    step = 0
    sqrt = int(math.sqrt(n) + 2)
    for expands in xrange(2, sqrt):
        # primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        # for expands in primes:
        # if expands >= sqrt:
            # break
        while n % expands == 0:
            step += expands
            n /= expands
    return step + (0 if n == 1 else n)
