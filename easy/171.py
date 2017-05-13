# coding=utf-8

"""Excel Sheet Column Number."""

from __future__ import print_function


def _solve(s):
    ans = 0
    for char in s:
        ans *= 26
        ans += ord(char) + -ord('A') + 1
    return ans


if __name__ == '__main__':
    print (_solve(''))
    print (_solve('A'))
    print (_solve('AA'))
    print (_solve('AAA'))
