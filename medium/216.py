# coding=utf-8

"""Combination Sum III.

>>> solve = _solve
>>> solve(3, 15)
[[1, 5, 9], [1, 6, 8], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 4, 8], [3, 5, 7], [4, 5, 6]]
"""


# 实际上不需要有细节优化就可以直接过了
def _solve(k, n):
    if n == 0:
        return []
    ans, digits = [], range(10)

    def _dfs(cur_n, count, arr, remainder):
        if remainder == 0:
            ans.append(arr)
            return
        if count == 0 or 9 - cur_n < count - 1:
            return
        if remainder > sum(digits[-1:-count - 1:-1]) or remainder < sum(digits[cur_n:cur_n + count]):
            return
        _dfs(cur_n + 1, count - 1, arr + [cur_n], remainder - cur_n)
        _dfs(cur_n + 1, count, arr, remainder)

    _dfs(1, k, [], n)
    return ans


# 一种比较常规的写法
def _solve1(k, n):
    ans, digits = [], range(10)

    def _dfs(arr, start, remainder):
        if len(arr) == k and remainder == 0:
            ans.append(arr)
            return
        for i in digits[start:]:
            _dfs(arr + [i], i + 1, remainder - i)

    _dfs([], 1, n)
    return ans


print _solve1(3, 15)
