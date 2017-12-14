# coding=utf-8

"""Subsets."""


# Bit Manipulation
def _solve(nums):
    res, length = [], len(nums)
    for i in xrange(1 << length):
        item = []
        for j in xrange(length):
            if (1 << j) & i:
                item.append(nums[j])
        res.append(item)
    return res


# Recursive (Backtracking)
def _solve1(nums):
    res, length = [], len(nums)

    def _dfs(cur, start):
        res.append(cur)
        for i in xrange(start, length):
            _dfs(cur + [nums[i]], i + 1)
    _dfs([], 0)
    return res


# Iterative
def _solve2(nums):
    res = [[]]
    for num in nums:
        res += [item + [num] for item in res]
    return res
