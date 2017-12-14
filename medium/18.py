# coding=utf-8

"""4Sum.

>>> solve = _solve1
>>> solve([0, 0, 0, 0, 0], 0)
[[0, 0, 0, 0]]
>>> solve([1, 0, -1, 0, -2, 2], 0)
[[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]
"""

# 此题通用的解决方法（k-sum）来说是是 N ^ (k - 1)
# 思路是先排序数组 如果 k=2，sum 复杂度为 n;否则将问题转化为 (k-1)-sum
# 此题不存在最坏情况下复杂度小于 n ^ 3 的算法（https://discuss.leetcode.com/topic/27445/lower-bound-n-3）

import collections


def _solve(nums, target):
    # sort 是为了 set 去重（加入 set 的 tuple 是有序的）
    nums.sort()
    two_sum, res, length = collections.defaultdict(list), set(), len(nums)
    for i in xrange(2, length):
        for j in xrange(i + 1, length):
            two_sum[nums[i] + nums[j]].append((i, j))
    for i in xrange(1, length - 2):
        for j in xrange(i):
            remain = target - nums[i] - nums[j]
            for i1, i2 in two_sum[remain]:
                if i1 > i:
                    res.add((nums[j], nums[i], nums[i1], nums[i2]))
    return map(list, res)


# 以下为通用解法，如果追求速度，可以加入大量的判断减枝
# 由于此题的 k=4，写成三次循环代码量也不大
def _solve1(nums, target):
    nums.sort()
    res, length = [], len(nums)

    def _k_sum(target, k, left, arr):
        right = length - 1
        if (right - left + 1) < k or target < nums[left] * k or target > nums[right] * k:
            return
        if k == 2:
            while left < right:
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    res.append(arr + [nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                elif two_sum < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in xrange(left, right - k + 2):
                if i == left or (i > left and nums[i] != nums[i - 1]):
                    _k_sum(target - nums[i], k - 1, i + 1, arr + [nums[i]])

    _k_sum(target, 4, 0, [])
    return res
