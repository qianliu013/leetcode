# coding=utf-8
"""Jewels and Stones.

>>> solve = _solve
>>> solve('aA', 'aAAbbbb')
3
>>> solve('z', 'ZZ')
0
"""


def _solve(J, S):
    jewels = set(J)
    return sum(ch in jewels for ch in S)
