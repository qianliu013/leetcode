# coding=utf-8

"""Integer Break.

>>> solve = _solve2
>>> [solve(i) for i in range(2, 14)]
[1, 2, 4, 6, 9, 12, 18, 27, 36, 54, 81, 108]
"""


# dp
def _solve(n):
    res = [1] * (n + 1)
    for i in xrange(2, n + 1):
        for j in xrange(1, i / 2 + 1):
            res[i] = max(max(res[j], j) * max(res[i - j], i - j), res[i])
    return res[n]


# 也可以数学证明或者打表找规律的方法使用如下两种方法
def _solve1(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    res = 1
    while n > 4:
        res *= 3
        n -= 3
    return n * res


def _solve2(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n % 3 == 0:
        return 3 ** (n / 3)
    if n % 3 == 1:
        return 4 * (3 ** ((n - 4) / 3))
    if n % 3 == 2:
        return 2 * (3 ** (n / 3))
