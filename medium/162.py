# coding=utf-8

"""Find Peak Element.

>>> solve = _solve
>>> _solve([1])
0
>>> _solve([2, 1])
0
>>> _solve([1, 2, 3, 1])
2
"""


# 对于数组 log(n) 的解法容易想到的是 二分，但是此题为什么能用二分呢？
# 其主要在于理解：两个限制条件 num[i] ≠ num[i+1]；num[-1] = num[n] = -∞ 保证了 peak 一定存在
# 即如果都是升序的，那么最后一项满足条件；都是降序的，第一项满足条件；否则由于相邻数不等，则一定存在 peak
# 理解题目，此题就很容易了
def _solve(nums):
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high) / 2
        if nums[mid] < nums[mid + 1]:
            low = mid + 1
        else:
            high = mid
    return low
