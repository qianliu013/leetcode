# coding=utf-8

"""Palindromic Substrings.

>>> solve = _solve
>>> solve()

"""


def _solve(s):
    length, res = len(s), 0
    for i in xrange(1, length):
        for j in xrange(0, length - i):
            if palindromic(i, ):
                res += 1
    print res
