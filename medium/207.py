# coding=utf-8
"""Course Schedule.

>>> solve = _solve1
>>> solve(2, [[1, 0]])
True
>>> solve(3, [[1, 0], [2, 0]])
True
>>> solve(3, [[0, 2], [1, 2], [2, 0]])
False
"""

import collections


# dfs：需要用于指示当前是否访问过的 visited, 可以使用一个额外的 cache 来缓存结果，以避免同个节点的多次访问
# 可以使用两个 set 或者 [False] * numCourses，也可以使用一个 int 数组，用不同的数字表示不同的状态
def _solve(numCourses, prerequisites):
    faker_start, graph = numCourses, collections.defaultdict(list)
    for end, start in prerequisites:
        graph[start].append(end)
    for start in graph.keys():
        graph[faker_start].append(start)
    cache = set()

    def _dfs(start, visited):
        if start in cache:
            return True
        else:
            if visited[start]:
                return False
            visited[start] = True
            for nxt in graph[start]:
                if not _dfs(nxt, visited):
                    return False
        cache.add(start)
        return True

    return _dfs(faker_start, [False] * (numCourses + 1))


# bfs：不断选取入度为 0 的节点迭代
def _solve1(numCourses, prerequisites):
    graph, indegree = collections.defaultdict(list), [0] * numCourses
    for end, start in prerequisites:
        graph[start].append(end)
        indegree[end] += 1
    queue = collections.deque([i for i in xrange(numCourses) if indegree[i] == 0])
    count = 0
    while queue:
        node = queue.pop()
        count += 1
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return count == numCourses
