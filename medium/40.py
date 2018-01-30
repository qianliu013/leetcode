# coding=utf-8
"""Combination Sum II.

>>> solve = _solve
>>> len(solve([1, 2, 2, 2, 2], 5))
1
>>> len(solve([10, 1, 2, 3, 3, 7, 6, 1, 5], 8))
7
>>> len(solve([1], 8))
0
"""


def _solve(candidates, target):
    candidates.sort()
    res, length = [], len(candidates)

    def _dfs(arr, remaining, start):
        if remaining == 0:
            res.append(list(arr))
        else:
            prev = candidates[0] - 1
            for i in xrange(start, length):
                new_remaining = remaining - candidates[i]
                if prev == candidates[i]:
                    continue
                prev = candidates[i]
                if new_remaining < 0:
                    break
                arr.append(candidates[i])
                _dfs(arr, new_remaining, i + 1)
                arr.pop()

    _dfs([], target, 0)
    return res


def _solve1(candidates, target):
    candidates.sort(reverse=True)
    last, total = [([], target)], 1
    for i, num in enumerate(candidates):
        if num == candidates[i - 1]:
            search_range = last[len(last) - total:]
        else:
            search_range = last[:]
        total = 0
        for arr, remaining in search_range:
            if remaining >= num:
                last.append((arr + [num], remaining - num))
                total += 1
    return [arr for arr, remaining in last if remaining == 0]
