# coding=utf-8

"""Single Number III.

>>> solve = _solve
>>> solve([1, 2, 1, 3, 2, 5])
[3, 5]
"""

import operator


def _solve(nums):
    xor_result = reduce(operator.xor, nums)
    mask = 1
    # 在其他语言可以写成
    # mask = xor_result & -xor_result
    # 或
    # mask = xor_result & ~(xor_result - 1)
    # 总之，是取最右边的非零位
    while xor_result & mask == 0:
        mask <<= 1
    a_num = reduce(operator.xor, [num for num in nums if num & mask])
    return [a_num, xor_result ^ a_num]
