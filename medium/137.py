# coding=utf-8

"""Single Number II.

>>> solve = _solve
>>> solve([1,1,1,2])
2
"""

import ctypes


# 这算一种通用做法，3 可以是任何数(>1)
def _solve(nums):
    return ctypes.c_int32((sum([1 << i for i in range(32) if len([num for num in nums if num & (1 << i)]) % 3]))).value


# 有限状态机 (0,0) -> (0,1) -> (1,0) -> (0,0)
# 三次重复，因此长度为 3
# 类似数电的内容，对此建模；只需要表示其中存在的状态即可，未存在的状态可以不去理会
# 代码中 tuple 表示为 (twos, ones)
def _solve1(nums):
    ones, twos = 0, 0
    for num in nums:
        ones = (ones ^ num) & (~twos)
        twos = (twos ^ num) & (~ones)
    return ones


# 另一种建模方法
def _solve2(nums):
    ones, twos, mask = 0, 0, 0
    for num in nums:
        twos |= (ones & num)
        ones ^= num
        mask = ones & twos
        ones &= ~mask
        twos &= ~mask
    return ones


# 另一种通用做法
# 参考自 https://discuss.leetcode.com/topic/455/constant-space-solution/46
def _solve3(nums):
    def _general_version(nums, k, l):
        head, k_bit = 0, [0] * k
        k_bit[0] = ~0
        for num in nums:
            head = k_bit[k - 1]
            for i in range(k - 1, 0, -1):
                k_bit[i] = (k_bit[i - 1] & num) | (k_bit[i] & ~num)
            k_bit[0] = (head & num) | (k_bit[0] & ~num)
        return k_bit[l]
    return _general_version(nums, 3, 1)
