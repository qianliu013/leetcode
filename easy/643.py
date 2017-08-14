# coding=utf-8

"""Maximum Average Subarray I.

>>> solve = _solve
>>> solve([1,12,-5,-6,50,3], 4)
12.75
"""


def _solve(nums, k):
    cur = ans = sum(nums[:k])
    for i, num in enumerate(nums[k:]):
        cur = cur - nums[i] + num
        ans = max(cur, ans)
    return ans * 1.0 / k
