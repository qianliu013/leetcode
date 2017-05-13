# coding=utf-8

"""Power of Three."""

from __future__ import print_function
import math


def _solve(n):
    return 3 ** int(round(math.log(abs(n), 3))) == n if n > 0 else False


def _solve1(n):
    return n > 0 and (3 ** 20) % n == 0


if __name__ == '__main__':
    print (_solve1(27))
