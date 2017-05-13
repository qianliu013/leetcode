# coding=utf-8

"""Distribute Candies."""


def _solve(candies):
    return min(len(candies) / 2, len(set(candies)))


if __name__ == '__main__':
    print _solve([1, 1, 2, 2, 3, 3])
    print _solve([1, 1, 2, 3])
    print _solve([1, 1, 1, 1])
