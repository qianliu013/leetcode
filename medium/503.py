# coding=utf-8

"""Next Greater Element II.

>>> solve = _solve1
>>> solve([1, 3, 0, 2, 1])
[3, -1, 2, 3, 3]
"""


# 0 -> n
def _solve(nums):
    stack, res = [], [-1] * len(nums)
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            res[stack.pop()] = num
        stack.append(i)
    for i, num in enumerate(nums):
        while stack and nums[stack[-1]] < num:
            res[stack.pop()] = num
    return res


# n -> 0
def _solve1(nums):
    stack, res, length = [], [None] * len(nums), len(nums)
    for i in xrange(length - 1, -length - 1, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        res[i] = nums[stack[-1]] if stack else -1
        stack.append(i)
    return res
