# coding=utf-8

"""Power of Four."""

from __future__ import print_function


def _solve(num):
    return bool(num & (num - 1) == 0 and num & 0x55555555)


# 证明
# (4^n-1) = (4-1) (4^(n-1) + 4^(n-2) + 4^(n-3) + ..... + 4 + 1)
# By induction: 4^(n+1) - 1 = 4 * 4^n -1 = 3 * 4^n + 4^n-1.
# The first is divided by 3, the second is proven by induction hypothesis
def _solve1(num):
    return num & num - 1 == 0 and (num - 1) % 3 == 0


if __name__ == '__main__':
    for i in range(-10, 100000):
        if _solve(i):
            print (i)
