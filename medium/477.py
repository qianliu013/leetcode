# coding=utf-8

"""Total Hamming Distance.

>>> solve = _solve1
>>> solve([4, 14, 2])
6
"""


def _solve(nums):
    sum_1, length = [], len(nums)
    for digit in xrange(32):
        sum_1.append(sum([num & (1 << digit) != 0 for num in nums]))
    return sum([count * (length - count) for count in sum_1])


# 1 line，参考 https://discuss.leetcode.com/topic/72149/python-via-strings
def _solve1(nums):
    return sum(bit_str.count('0') * bit_str.count('1') for bit_str in zip(*map('{:032b}'.format, nums)))
