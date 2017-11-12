# coding=utf-8

"""Count Binary Substrings.

>>> solve = _solve
>>> print solve('00110011')
6
>>> print solve('10101')
4
"""


def _solve(s):
    res, prev, cur = 0, 0, 1
    for i, char in enumerate(s[1:]):
        if char != s[i]:
            res += min(prev, cur)
            prev, cur = cur, 1
        else:
            cur += 1
    return res + min(prev, cur)
