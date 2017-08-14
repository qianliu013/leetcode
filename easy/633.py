# coding=utf-8

"""Sum of Square Numbers.

>>> solve = _solve2
>>> solve(3)
False
>>> solve(5)
True
"""

import math


def _solve(c):
    left, right = 0, int(math.sqrt(c) + 0.1)
    while left <= right:
        other = c - left * left - right * right
        if other == 0:
            return True
        elif other < 0:
            right = min(right - 1, int(math.sqrt(c - left * left) + 0.1))
        else:
            left = max(left + 1, int(math.sqrt(c - right * right) + 0.1))
    return False


def _solve1(c):
    left, right = 0, int(math.sqrt(c) + 0.1)
    while left <= right:
        other = c - left * left - right * right
        if other == 0:
            return True
        elif other > 0:
            left += 1
        else:
            right -= 1
    return False


# Fermat Theorem: https://leetcode.com/articles/sum-of-square-numbers/
def _solve2(c):
    for i in range(2, int(math.sqrt(c) + 1)):
        count = 0
        if c % i == 0:
            while c % i == 0:
                count += 1
                c /= i
            if i % 4 == 3 and count & 1 != 0:
                return False
    return c % 4 != 3
