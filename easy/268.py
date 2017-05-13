# coding=utf-8

"""Missing Number."""

from __future__ import print_function


# 求和也可以
def _solve(nums):
    miss_number = 0
    for i in xrange(1, len(nums) + 1):
        miss_number ^= i
    for num in nums:
        miss_number ^= num
    return miss_number


if __name__ == '__main__':
    print (_solve([0, 1, 3]))
