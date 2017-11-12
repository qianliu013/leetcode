# coding=utf-8

"""Minimum Number of Arrows to Burst Balloons.

>>> solve = _solve
>>> solve([[10, 16], [2, 8], [1, 6], [7, 12]])
2
>>> solve([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]])
2
"""


def _solve(points):
    res, border = 0, -float('inf')
    for left, right in sorted(points, key=lambda point: point[1]):
        if left > border:
            res += 1
            border = right
    return res
