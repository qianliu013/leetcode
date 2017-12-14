# coding=utf-8

"""Redundant Connection.

>>> solve = _solve1
>>> solve([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
[1, 4]
"""

import collections


# 最初的思路，对于只有一个环的图，那么只要随意从一点出发，遍历，找到那个环即可
# 然后遍历环上的边去得到最后加入的一条边，显然这种思路写起来略有点麻烦
def _solve(edges):
    vertices, index_dict = collections.defaultdict(list), {}
    for i, (v1, v2) in enumerate(edges):
        vertices[v1].append(v2)
        vertices[v2].append(v1)
        index_dict[(v1, v2)] = index_dict[(v2, v1)] = i
    visited = {edges[0][0]}
    circle = []

    def _dfs(path):
        for v in vertices[path[-1]]:
            if v != path[-2]:
                if v in visited:
                    circle.append(path + [v])
                    return
                else:
                    visited.add(v)
                    _dfs(path + [v])

    _dfs([0, edges[0][0]])
    ans = 0
    start = circle[0].index(circle[0][-1])
    for i in xrange(start, len(circle[0]) - 1):
        ans = max(ans, index_dict[(circle[0][i], circle[0][i + 1])])
    return edges[ans]


# 使用并查集的写法要简单很多，只要检测新加的两条边不在同一个部分内即可
# 代码参考自：https://discuss.leetcode.com/topic/104729/10-line-java-solution-union-find
# 一种五行的写法可见：https://discuss.leetcode.com/topic/104691/unicode-find-5-short-lines
def _solve1(edges):
    def _find(v):
        if v != parent[v]:
            parent[v] = _find(parent[v])
        return parent[v]

    parent = range(0, 1001)
    for v1, v2 in edges:
        parent_v1, parent_v2 = _find(v1), _find(v2)
        if parent_v1 == parent_v2:
            return [v1, v2]
        parent[parent_v2] = parent_v1
