# coding=utf-8
"""Letter Case Permutation.

>>> solve = _solve
>>> solve('a1b2')
['A1B2', 'A1b2', 'a1B2', 'a1b2']
>>> solve('12345')
['12345']
"""


# 代码来自 https://leetcode.com/problems/letter-case-permutation/discuss/115509/Python-simple-solution-(7-lines)
def _solve(S):
    res = ['']
    for ch in S:
        if ch.isalpha():
            res = [i + j for i in res for j in [ch.upper(), ch.lower()]]
        else:
            res = [i + ch for i in res]
    return res
