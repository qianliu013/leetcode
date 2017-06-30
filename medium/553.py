# coding=utf-8

"""Optimal Division.

>>> _solve([1])
'1'
>>> _solve([1, 2])
'1/2'
>>> _solve([1000,100,10,2])
'1000/(100/10/2)'
"""


def _solve(nums):
    if len(nums) == 1:
        return str(nums[0])
    elif len(nums) == 2:
        return str(nums[0]) + '/' + str(nums[1])
    else:
        return str(nums[0]) + "/(" + "/".join([str(num) for num in nums[1:]]) + ")"
