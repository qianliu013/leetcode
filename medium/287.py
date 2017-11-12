# coding=utf-8

"""Find the Duplicate Number.

>>> solve = _solve2
>>> solve([1, 4, 2, 3, 1])
1
"""


def _solve(nums):
    res = 0
    for i in xrange(32):
        tmp, origin_sum, nums_sum = 1 << i, 0, 0
        for nth, num in enumerate(nums):
            origin_sum += bool(tmp & nth)
            nums_sum += bool(tmp & num)
        res += tmp * (nums_sum > origin_sum)
    return res


def _solve1(nums):
    low, high = 1, len(nums) - 1
    while low < high:
        mid = low + (high - low) / 2
        count = 0
        for num in nums:
            count += num <= mid
        if count <= mid:
            low = mid + 1
        else:
            high = mid
    return low


def _solve2(nums):
    slow, fast = nums[0], nums[nums[0]]
    while slow != fast:
        slow, fast = nums[slow], nums[nums[fast]]
    fast = 0
    while slow != fast:
        slow, fast = nums[slow], nums[fast]
    return slow
