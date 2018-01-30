# coding=utf-8

"""Increasing Subsequences.

>>> nums = [4, 6, 7, 7, 4, 7]
>>> len(_solve(nums)) == len(_solve1(nums)) == len(_solve2(nums)) ==  len(_solve3(nums)) == 14
True
"""

import collections


def _solve(nums):
    dp = collections.defaultdict(set)
    for num in nums:
        if num not in dp:
            dp[num].add((num,))
        else:
            dp[num] |= set([a_list + (num,) for a_list in dp[num]])
        for end in dp:
            if end < num:
                dp[num] |= set([a_list + (num,) for a_list in dp[end]])
    return sum([[list(a_tuple) for a_tuple in a_set if len(a_tuple) > 1] for a_set in dp.values()], [])


# 其实上述的 dict 完全没必要，可以只用一个包含全部当前结果的 set；虽然暴力，但写法十分简洁
# 代码来自 https://discuss.leetcode.com/topic/76282/simple-python 思路
def _solve1(nums):
    subs = {()}
    for num in nums:
        subs |= {sub + (num,)
                 for sub in subs
                 if not sub or sub[-1] <= num}
    return [sub for sub in subs if len(sub) >= 2]


# 上述的方法都是建立于可以 list 的 set，如果不用 list 的 set 呢？
# 一种思路是使用 backtrack，类似于之前计算所有组合的思想
def _solve2(nums):
    res = []

    def _dfs(start, cur):
        if len(cur) > 1:
            res.append(list(cur))
        used = set()
        for i in xrange(start, len(nums)):
            if nums[i] in used:
                continue
            if len(cur) == 0 or cur[-1] <= nums[i]:
                used.add(nums[i])
                cur.append(nums[i])
                _dfs(i + 1, cur)
                cur.pop()

    _dfs(0, [])
    return res


# 其实可以改进之前的 dp 方法，想办法不用 set 去重
def _solve3(nums):
    n, seen = len(nums), set()
    dp, ans = [[] for i in range(n)], []
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if nums[j] <= nums[i]:
                for each in dp[j]:
                    nxt = each + [nums[i]]
                    dp[i].append(nxt)
                    ans.append(nxt)
            if nums[j] == nums[i]:
                break
        if nums[i] not in seen:
            dp[i].append([nums[i]])
            seen.add(nums[i])
    return ans
