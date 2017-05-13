# coding=utf-8

"""Happy Number."""

from __future__ import print_function


def _solve(n):
    result = {}
    digit_square_sum = n
    while digit_square_sum != 1:
        digit_square_sum = reduce(lambda acc, cur: acc + cur ** 2, [
            int(digit) for digit in str(digit_square_sum)
        ], 0)
        if digit_square_sum in result:
            return False
        result[digit_square_sum] = 1
    return True


def _solve1(n):
    result = []
    while n not in result:
        result.append(n)
        n = sum([int(x) ** 2 for x in str(n)])
    return n == 1


if __name__ == '__main__':
    print (_solve(19))
    print (_solve1(19))
