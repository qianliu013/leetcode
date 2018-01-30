# coding=utf-8

"""Min Cost Climbing Stairs.

>>> solve = _solve
>>> solve([10, 15, 20])
15
>>> solve([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
6
"""


def _solve(cost):
    prev, cur = cost[0], cost[1]
    for each in cost[2:]:
        prev, cur = cur, min(prev, cur) + each
    return min(prev, cur)
