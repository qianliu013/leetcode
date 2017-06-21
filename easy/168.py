# coding=utf-8

"""Excel Sheet Column Title."""

from __future__ import print_function


def _solve(n):
    ans = ''
    start = ord('A')
    while n > 0:
        n -= 1
        ans = chr(start + n % 26) + ans
        n /= 26
    return ans


if __name__ == '__main__':
    for i in range(60):
        print (_solve(i), end=' ')
