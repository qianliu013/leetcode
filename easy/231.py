# coding=utf-8

"""Power of Two."""

from __future__ import print_function


def _solve(n):
    return n > 0 and not(n & (n - 1))


if __name__ == '__main__':
    for i in range(100000):
        if _solve(i):
            print (i)
