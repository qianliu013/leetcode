# coding=utf-8

"""Base 7."""

from __future__ import print_function


def _convert_to_base_7(num):
    if not num:
        return '0'
    ans = ''
    pos_num = abs(num)
    while pos_num:
        ans = str(pos_num % 7) + ans
        pos_num /= 7
    return ('-' if num < 0 else '') + ans


if __name__ == '__main__':
    print (_convert_to_base_7(100))
    print (_convert_to_base_7(-7))
