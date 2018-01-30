# coding=utf-8
"""House Robber II.

>>> solve = _solve
>>> solve([])
0
>>> solve([2])
2
>>> solve([1, 2])
2
"""


def _solve(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    steal_first = [0, nums[0]]
    for num in nums[1:]:
        steal_first[0], steal_first[1] = steal_first[1], max(steal_first[1], steal_first[0] + num)
    steal_second = [0, 0]
    for num in nums[1:]:
        steal_second[0], steal_second[1] = steal_second[1], max(steal_second[1], steal_second[0] + num)
    return max(steal_first[0], steal_second[1])
