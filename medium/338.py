# coding=utf-8

"""Counting Bits."""

from __future__ import print_function


def _solve0(num):
    return [bin(i).count('1') for i in xrange(num + 1)]


def _solve1(num):
    if num == 0:
        return [0]
    ans = [0] * (num + 1)
    ans[1] = 1
    digits, mid = 1, 1
    while (1 << (digits + 1)) < num + 2:
        mid = 1 << digits
        for i in xrange(mid):
            ans[i + mid] = ans[i] + 1
        digits += 1
    mid *= 2
    for i in range(num - mid + 1):
        ans[i + mid] = ans[i] + 1
    return ans


def _solve2(num):
    ans = [0] * (num + 1)
    offset = 1
    for i in xrange(1, num + 1):
        if offset * 2 == i:
            offset *= 2
        ans[i] = 1 + ans[i - offset]
    return ans


def _solve3(num):
    ans = [0] * (num + 1)
    for i in xrange(1, num + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


def _solve4(num):
    ans = [0] * (num + 1)
    for i in xrange(1, num + 1):
        ans[i] = ans[i & (i - 1)] + 1
    return ans


if __name__ == '__main__':
    for end in range(100):
        if _solve0(end) != _solve3(end):
            print (end, _solve0(end), _solve1(end))
            break
