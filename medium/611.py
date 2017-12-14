# coding=utf-8

"""Valid Triangle Number.

>>> solve = _solve
>>> solve([2,2,3,4])
3
"""


def _solve(nums):
    nums.sort()
    res, length = 0, len(nums)
    for i1 in xrange(length - 2):
        if nums[i1] == 0:
            continue
        i3 = i1 + 2
        for i2 in xrange(i1 + 1, length - 1):
            while i3 < length and nums[i1] + nums[i2] > nums[i3]:
                i3 += 1
            res += i3 - i2 - 1
    return res


# 更易理解、快的一种写法
def _solve1(nums):
    res, length = 0, len(nums)
    nums.sort(reverse=True)
    for i, target in enumerate(nums):
        left, right = i + 1, length - 1
        while left < right:
            if nums[left] + nums[right] > target:
                res += right - left
                left += 1
            else:
                right -= 1
    return res
