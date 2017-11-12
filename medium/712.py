# coding=utf-8

"""Minimum ASCII Delete Sum for Two Strings.

>>> solve = _solve
>>> solve("sea", "eat")
231
>>> solve('delete', 'leet')
403
"""


# 思路同 lCS，参考 583 题解
def _solve(s1, s2):
    len2 = len(s2)
    dp = [0] * (len2 + 1)
    for char1 in s1:
        tmp = [0] * (len2 + 1)
        for i, char2 in enumerate(s2):
            tmp[i + 1] = max(dp[i + 1], tmp[i], dp[i] + (char1 == char2) * 2 * ord(char1))
        dp = tmp
    return sum(map(ord, s1 + s2)) - dp[-1]
