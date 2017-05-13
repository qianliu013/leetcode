# coding=utf-8

"""First Unique Character in a String."""

from __future__ import print_function


def _solve(s):
    result = {}
    for char in s:
        result[char] = result.get(char, 0) + 1
    for index, char in enumerate(s):
        if result[char] == 1:
            return index
    return -1


if __name__ == '__main__':
    print (_solve('l'))
