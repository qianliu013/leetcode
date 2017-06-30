# coding=utf-8

"""Find All Duplicates in an Array.

>>> _solve1([4,3,2,7,8,2,3,1])
[2, 3]
"""


def _solve(nums):
    length = len(nums)
    for num in nums:
        nums[(num - 1) % length] += length
    return [(i + 1) for i, num in enumerate(nums) if num > 2 * length]


def _solve1(nums):
    ans = []
    for num in nums:
        if nums[abs(num) - 1] < 0:
            ans.append(abs(num))
        nums[abs(num) - 1] *= -1
    return ans
