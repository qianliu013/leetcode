# coding=utf-8
"""Partition Labels.

>>> solve = _solve
>>> solve('ababcbacadefegdehijhklij')
[9, 7, 8]
"""


def _solve(S):
    indexes, res = {}, []
    prev_i = end = 0
    for i, ch in enumerate(S):
        indexes[ch] = i
    for i, ch in enumerate(S):
        end = max(end, indexes[ch])
        if i == end:
            res.append(end - prev_i + 1)
            prev_i = end + 1
    return res
