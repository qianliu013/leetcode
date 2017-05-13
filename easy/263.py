# coding=utf-8

"""Ugly Number."""

from __future__ import print_function


def _solve(num):
    if num <= 0:
        return False
    primes = [2, 3, 5]
    for prime in primes:
        while num % prime == 0:
            num /= prime
    return num == 1


if __name__ == '__main__':
    for i in xrange(10000):
        print (i, _solve(i))
