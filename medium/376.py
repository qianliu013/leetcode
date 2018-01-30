# coding=utf-8
"""Wiggle Subsequence.

>>> solve = _solve
>>> solve([1, 1])
1
>>> solve([1, 7, 4, 9, 2, 5])
6
>>> solve([1, 1, 7, 4, 5, 5])
4
"""


# 其实很容想到用贪心来做
# 最初的写法
def _solve(nums):
    if len(nums) < 2:
        return len(nums)
    news = [nums[0]]
    for num in nums[1:]:
        if num != news[-1]:
            news.append(num)
    nums = news
    if len(nums) < 2:
        return len(nums)
    ans, flag, idx, length = 1, nums[0] < nums[1], 0, len(nums)
    while idx + 1 < length:
        while idx + 1 < length and ((nums[idx] < nums[idx + 1]) == flag):
            idx += 1
        ans += 1
        flag = not flag
    return ans


# 更加简洁的写法
def _solve1(nums):
    if len(nums) < 2:
        return len(nums)
    prev_diff = nums[1] - nums[0]
    count = 2 if prev_diff != 0 else 1
    for i in xrange(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and prev_diff <= 0) or (diff < 0 and prev_diff >= 0):
            count += 1
            prev_diff = diff
    return count


# 其实，也可以用一个差值数组来表示相邻两个数的差，if diff[i] * diff[i - 1] < 0: ans += 1
# 代码可参考： https://discuss.leetcode.com/topic/52468/python-solution-48ms


# 从 dp 的角度考虑也可以
def _solve2(nums):
    if len(nums) < 2:
        return len(nums)
    down = up = 1
    for i in xrange(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up = down + 1
        elif nums[i] < nums[i - 1]:
            down = up + 1
    return max(down, up)
