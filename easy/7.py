# coding=utf-8

"""Reverse Integer."""

from __future__ import print_function


def _solve(x):
    flag = 1 if x > 0 else -1
    reverse_str_abs_n = str(abs(x))[::-1]
    if int(reverse_str_abs_n) > 2147483647:
        return 0
    return int(reverse_str_abs_n) * flag


# 注意在 python 不溢出
# 此外取余与其他语言不同,在 Python 中 (-14 % 10) = (- 10 * 2 + 6) % 10 = 6
# C,C++ 等 -14 % 10 = -4
def _solve1(x):
    flag = 1 if x > 0 else -1
    abs_x = flag * x
    result = 0
    max_int = (1 << 31) - 1
    while abs_x:
        result = result * 10 + abs_x % 10
        if result > max_int:
            return 0
        abs_x /= 10
    return flag * result


if __name__ == '__main__':
    print (_solve(2147483647))
    print (_solve1(2147483647))
    print (_solve1(-21))
    print (_solve1(0))
