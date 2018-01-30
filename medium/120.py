# coding=utf-8
"""Triangle.

>>> solve = _solve
>>> solve([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
11
"""


def _solve(triangle):
    cur = list(triangle[-1])
    for layer in triangle[:-1][::-1]:
        for i in xrange(len(layer)):
            cur[i] = layer[i] + min(cur[i], cur[i + 1])
    return cur[0]
