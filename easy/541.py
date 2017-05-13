# coding=utf-8

"""Reverse String II."""

from __future__ import print_function


def _solve(s, k):
    left = 0
    ans = ''
    length = len(s)
    while left < length:
        mid = min(left + k, length)
        right = min(left + 2 * k, length)
        ans += s[left:mid][::-1]
        ans += s[mid:right]
        left += 2 * k
    return ans


if __name__ == '__main__':
    print (_solve('abcdefg', 2))
