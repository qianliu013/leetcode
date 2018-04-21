# coding=utf-8
"""Maximum Product Subarray.

>>> solve = _solve
>>> solve([1, 2, 3])
6
>>> solve([1, -2, 3])
3
"""


def _solve(nums):
    ans = max_dp = min_dp = nums[0]
    for num in nums[1:]:
        max_dp, min_dp = max(min_dp * num, max_dp * num, num), min(max_dp * num, min_dp * num, num)
        ans = max(ans, max_dp)
    return ans


# 稍微处理下 num 的正负
def _solve1(nums):
    ans = max_dp = min_dp = nums[0]
    for num in nums[1:]:
        if num < 0:
            max_dp, min_dp = min_dp, max_dp
        max_dp = max(max_dp * num, num)
        min_dp = min(min_dp * num, num)
        ans = max(ans, max_dp)
    return ans
