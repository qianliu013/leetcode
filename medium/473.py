# coding=utf-8
"""Matchsticks to Square.

>>> solve = _solve
>>> solve([])
False
>>> solve([1, 1, 2, 2, 2])
True
>>> solve([3, 3, 3, 4, 4])
False
"""


# 此题即 698. Partition to K Equal Sum Subsets 的简化版本，思路来源可参考 698.py
def _solve(nums):
    target, remainder = divmod(sum(nums), 4)
    if remainder or not target:
        return False
    length, used = len(nums), [False] * len(nums)
    nums.sort(reverse=True)

    def _dfs(cur, start, nth):
        if nth == 0:
            return True
        if cur == target:
            return _dfs(0, 0, nth - 1)
        if cur > target:
            return False
        for i in xrange(start, length):
            if not used[i]:
                used[i] = True
                if _dfs(cur + nums[i], i + 1, nth):
                    return True
                used[i] = False
        return False

    return _dfs(0, 0, 4)


def _solve1(nums):
    target, remainder = divmod(sum(nums), 4)
    if remainder or not target:
        return False
    length, cache = len(nums), {0: True}
    nums.sort(reverse=True)

    def _dfs(state, remaining):
        if state not in cache:
            need = (remaining - 1) % target + 1
            cache[state] = any(
                _dfs(state ^ (1 << i), remaining - nums[i]) for i in xrange(length)
                if state & (1 << i) and nums[i] <= need)
        return cache[state]

    return _dfs((1 << length) - 1, 4 * target)


def _solve2(nums):
    target, remainder = divmod(sum(nums), 4)
    nums.sort()
    if remainder or not target or nums[-1] > target:
        return False
    length = len(nums)
    dp = [-1] * (1 << length)
    dp[0] = 0
    for state in xrange(1 << length):
        if dp[state] == -1:
            continue
        for i, num in enumerate(nums):
            nxt = (1 << i) | state
            if nxt != state and dp[nxt] == -1:
                if num <= target - (dp[state] % target):
                    dp[nxt] = dp[state] + num
                else:
                    break
    return dp[-1] != -1
