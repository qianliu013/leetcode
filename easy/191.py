# coding=utf-8

"""Number of 1 Bits."""

from __future__ import print_function

# 一些巧妙地位运算法可参考： https://en.wikipedia.org/wiki/Hamming_weight


def _solve(n):
    return bin(n).count('1')


def _solve1(n):
    ans = 0
    while n:
        n &= n - 1
        ans += 1
    return ans


if __name__ == '__main__':
    print (_solve(11))
    print (_solve1(11))
