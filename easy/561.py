# coding=utf-8

"""Array Partition I."""


def _solve(nums):
    return sum(sorted(nums)[::2])


if __name__ == '__main__':
    print (_solve([11, 12, 5, 1, 7, 6, 19, 4]))
