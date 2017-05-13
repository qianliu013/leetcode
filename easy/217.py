# coding=utf-8

"""Contains Duplicate."""

from __future__ import print_function
import collections


# 更简单写法
# return len(nums) != len(set(nums))
def _solve(nums):
    return reduce(lambda x, y: x | (y > 1),
                  collections.Counter(nums).values(), False)


if __name__ == '__main__':
    print (_solve([]))
    print (_solve([1]))
    print (_solve([1, 1]))
    print (_solve([1, 2]))
