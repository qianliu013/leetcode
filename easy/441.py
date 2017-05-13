# coding=utf-8

"""Arranging Coins."""

import math


def _solve(n):
    return int(math.sqrt(2 * n + 0.25) - 0.5)


if __name__ == '__main__':
    for i in range(16):
        print i, _solve(i)
