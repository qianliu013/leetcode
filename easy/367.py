# coding=utf-8

"""Valid Perfect Square."""

import math


def _solve(num):
    start = 0
    end = num
    while start <= end:
        mid = start + (end - start) / 2
        square = mid * mid
        if square == num:
            return True
        if square > num:
            end = mid - 1
        if square < num:
            start = mid + 1
    return False


def _solve1(num):
    i = 1
    while num > 0:
        num -= i
        i += 2
    return num == 0


def _solve2(num):
    x = num
    while x * x > num:
        x = (x + num / x) >> 1
    return x * x == num


if __name__ == '__main__':
    for i in range(10000):
        root = int(math.sqrt(i))
        if (root ** 2 == i) != _solve2(i):
            print (i)
