# coding=utf-8

"""Valid Anagram."""


def _solve(s, t):
    return sorted(s) == sorted(t)
