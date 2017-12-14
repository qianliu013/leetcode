# coding=utf-8

"""Combination Sum.

>>> solve = _solve1
>>> solve([2, 3, 6, 7], 7)
[[2, 2, 3], [7]]
"""


def _solve(candidates, target):
    candidates.sort()
    dp = [[[]]] + [[] for i in xrange(target)]
    for num in candidates:
        for i in xrange(num, target + 1):
            remaining = i - num
            if dp[remaining]:
                dp[i].extend([a_list + [num] for a_list in dp[remaining]])
    return dp[-1]


def _solve1(candidates, target):
    candidates.sort()
    res, length = [], len(candidates)

    def _dfs(arr, remaining, start):
        if remaining == 0:
            res.append(list(arr))
        else:
            for i in xrange(start, length):
                new_remaining = remaining - candidates[i]
                if new_remaining < 0:
                    break
                arr.append(candidates[i])
                _dfs(arr, new_remaining, i)
                arr.pop()

    _dfs([], target, 0)
    return res
