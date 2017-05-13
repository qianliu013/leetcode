# coding=utf-8

"""Roman to Integer."""

from __future__ import print_function


def _solve(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return reduce(lambda ans, index: (-1 if roman[s[index]] < roman[s[
        index + 1]] else 1) * roman[s[index]] + ans, range(0, len(s) - 1), 0) \
        + roman[s[-1]]


if __name__ == '__main__':
    print (_solve('MCMLIV'))
    print (_solve('DCXXI'))
