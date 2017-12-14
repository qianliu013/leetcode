# coding=utf-8

"""Evaluate Division.

>>> solve = _solve
>>> solve([["a", "b"], ["b", "c"]], [2.0, 3.0], [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]])
[6.0, 0.5, -1.0, 1.0, -1.0]
"""

# 这道题并不难，但是写起来相对繁琐一些
# 输入的 equation 可以认为是两个点和一条边，那么整体的 equations 可以认为构成了多个独立的无向连通图
# 任意两个节点之间的值都可以求到
# 于是自然可以想到并查集来求，只要知道任意节点到其 parent 的值，既可以求到任意节点间的值
# 代码可以参考 https://discuss.leetcode.com/topic/58577/0ms-c-union-find-solution-easy-to-understand
# 当然写并查集代码比较多，直接深搜并用 set 判重也可以
# 下面的方法是直接预处理得到所有可能的值；更常见的方法是只根据 queries 来求
# 如：https://discuss.leetcode.com/topic/58312/c-0ms-hash-dfs-solution


import collections
import itertools


def _solve(equations, values, queries):
    res = collections.defaultdict(dict)
    for i, (key1, key2) in enumerate(equations):
        res[key1][key1] = res[key2][key2] = 1.0
        res[key1][key2] = values[i]
        res[key2][key1] = 1 / values[i]

    visited = set()

    def _dfs(origin, prev):
        for key in res[prev].keys():
            if key not in visited:
                res[origin][key] = res[origin][prev] * res[prev][key]
                res[key][origin] = 1 / res[origin][key]
                visited.add(key)
                _dfs(origin, key)

    for key in res:
        visited = {key}
        _dfs(key, key)

    ans = []

    for key1, key2 in queries:
        if key1 in res and key2 in res[key1]:
            ans.append(res[key1][key2])
        else:
            ans.append(-1.0)

    return ans


# 此题的形式其实很容易联想到最短路劲中的
# [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)
# 以下代码来自
# https://discuss.leetcode.com/topic/58482/9-lines-floyd-warshall-in-python
def _solve1(equations, values, queries):
    quot = collections.defaultdict(dict)
    for (num, den), val in zip(equations, values):
        quot[num][num] = quot[den][den] = 1.0
        quot[num][den] = val
        quot[den][num] = 1 / val
    for k, i, j in itertools.permutations(quot, 3):
        if k in quot[i] and j in quot[k]:
            quot[i][j] = quot[i][k] * quot[k][j]
    return [quot[num].get(den, -1.0) for num, den in queries]
