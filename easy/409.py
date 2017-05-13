# coding=utf-8

"""Longest Palindrome."""

from __future__ import print_function
import collections


def _solve(s):
    result = {}
    ans = 0
    single = False
    for char in s:
        result[char] = result.get(char, 0) + 1
    for char in result:
        if result[char] % 2:
            ans += result[char] - 1
            single = True
        else:
            ans += result[char]
    return ans + (1 if single else 0)


def _solve1(s):
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)


if __name__ == '__main__':
    print (_solve('abccccdd'))
    print (_solve('dd'))
    print (_solve1('dd'))
