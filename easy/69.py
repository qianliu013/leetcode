# coding=utf-8

"""Sqrt(x)."""

from __future__ import print_function

import math


def _solve(x):
    start, end = 1, x
    # 可以使用除法来避免其他语言溢出的问题
    while start <= end:
        mid = start + (end - start) / 2
        square = mid * mid
        if square == x:
            return mid
        if square < x:
            start = mid + 1
        if square > x:
            end = mid - 1
    return start - 1


def _solve1(x):
    if x == 0:
        return x
    sqrt = x
    while sqrt > x / sqrt:
        sqrt = (sqrt + x / sqrt) / 2
    return sqrt


def _solve2(x):
    ans = 0
    bit = 1 << 16
    while bit:
        ans |= bit
        if ans * ans > x:
            ans ^= bit
        bit >>= 1
    return ans


if __name__ == '__main__':
    for i in range(2000):
        if _solve2(i) != int(math.sqrt(i)):
            print (i, _solve2(i), int(math.sqrt(i)))
