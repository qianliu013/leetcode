# coding=utf-8

"""Product of Array Except Self.

>>> solve = _solve1
>>> solve([1, 2, 3, 4])
[24, 12, 8, 6]
"""


def _solve(nums):
    ans = [1] * len(nums)
    for i in xrange(len(nums) - 2, -1, -1):
        ans[i] = ans[i + 1] * nums[i + 1]
    prev_multi = 1
    for i in range(1, len(nums)):
        prev_multi *= nums[i - 1]
        ans[i] = ans[i] * prev_multi
    return ans


# 不使用中间变量
def _solve1(nums):
    ans = [1] * len(nums)
    for i in xrange(len(nums) - 2, -1, -1):
        ans[i] = ans[i + 1] * nums[i + 1]
    # 使用最后一个值来做为中间值
    for i in range(0, len(nums) - 1):
        ans[i] = ans[i] * ans[-1]
        ans[-1] *= nums[i]
    return ans


# one pass
def _solve2(nums):
    length = len(nums)
    left, right, res = 1, 1, [1] * len(nums)
    for i in range(length):
        res[i] *= left
        res[length - i - 1] *= right
        left *= nums[i]
        right *= nums[length - i - 1]
    return res
