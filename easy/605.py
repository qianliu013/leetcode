# coding=utf-8

"""Can Place Flowers."""

from __future__ import print_function


def _solve(flowerbed, n):
    dummy = [0] + flowerbed + [0]
    for i in xrange(1, len(flowerbed) + 1):
        if dummy[i - 1] == 0 and dummy[i] == 0 and dummy[i + 1] == 0:
            n -= 1
            dummy[i] = 1
    return n < 1


# 不修改原数组
def _solve1(flowerbed, n):
    first, last, dummy = 1, len(flowerbed), [0] + flowerbed + [0]
    while first <= last:
        if dummy[first - 1] + dummy[first] + dummy[first + 1] == 0:
            n -= 1
            dummy[first] = 1
            first += 1
        first += 1
    return n < 1


if __name__ == '__main__':
    print (_solve1([1], 0))
    print (_solve1([1], 1))
    print (_solve1([0, 1], 1))
    print (_solve1([1, 0], 1))
    print (_solve1([0, 0], 1))
    print (_solve1([0, 0], 2))
    print (_solve1([1, 0, 0, 0, 1], 1))
    print (_solve1([1, 0, 0, 0, 1], 2))
