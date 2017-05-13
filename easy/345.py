# coding=utf-8

"""Reverse Vowels of a String."""

from __future__ import print_function
import re


def _solve(s):
    front = 0
    end = -1
    length = len(s)
    s = list(s)
    vowels = 'aeiouAEIOU'
    while front - end <= length:
        if s[front] in vowels and s[end] in vowels:
            s[front], s[end] = s[end], s[front]
            front += 1
            end -= 1
        if front == length or end == -length - 1:
            break
        if s[front] not in vowels:
            front += 1
        if s[end] not in vowels:
            end -= 1
    return ''.join(s)


if __name__ == '__main__':
    print (_solve(''))
    print (_solve('a.'))
    print (_solve('.a'))
    print (_solve('aeui'))
    print (_solve('race a car'))
