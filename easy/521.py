# coding=utf-8

"""Longest Uncommon Subsequence I."""

from __future__ import print_function


def _solve(a, b):
    return -1 if a == b else max(len(a), len(b))


if __name__ == '__main__':
    print (_solve('aaa', 'aaa'))
