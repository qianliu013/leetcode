# coding=utf-8

"""Valid Palindrome."""

from __future__ import print_function


def _solve(s):
    filter_str = [char.capitalize() for char in s if char.isalnum()]
    return filter_str == filter_str[::-1]


def _solve1(s):
    start, end = 0, len(s) - 1
    while start < end:
        if not s[start].isalnum():
            start += 1
        elif not s[end].isalnum():
            end -= 1
        else:
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
    return True


if __name__ == '__main__':
    print (_solve1(''))
    print (_solve1(' '))
    print (_solve1('A man, a plan, a canal: Panama'))
    print (_solve1('123321'))
    print (_solve1('race a car'))
