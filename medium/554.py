# coding=utf-8

"""Brick Wall.

>>> solve = _solve
>>> solve([[1],[1],[1]])
3
"""


import collections


def _solve(wall):
    res = collections.defaultdict(int)
    for row in wall:
        length = 0
        for brick in row[:-1]:
            length += brick
            res[length] += 1
    return len(wall) - max(res.values() + [0])
