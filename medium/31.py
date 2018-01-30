# coding=utf-8
"""Next Permutation.

>>> solve = _solve
>>> nums = [1, 2, 3]; solve(nums); nums
[1, 3, 2]
>>> nums = [3, 2, 1]; solve(nums); nums
[1, 2, 3]
>>> nums = [1, 1, 5]; solve(nums); nums
[1, 5, 1]
"""


def _solve(nums):
    length = len(nums)
    for i in xrange(length - 1, 0, -1):
        if nums[i - 1] < nums[i]:
            break
    else:
        i = 0
    if i > 0:
        for j in xrange(length - 1, i - 1, -1):
            if nums[j] > nums[i - 1]:
                break
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
    j = length - 1
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1
    return nums
