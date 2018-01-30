# coding=utf-8
"""Network Delay Time.

>>> solve = _solve
>>> solve([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)
2
"""

import collections
import heapq


# Dijkstra's Algorithm
def _solve(times, N, K):
    adj = [[] for _ in xrange(N + 1)]
    for u, to, w in times:
        adj[u].append((to, w))
    h_queue, dist = [], [float('inf')] * (N + 1)
    dist[K] = 0
    heapq.heappush(h_queue, (0, K))
    while h_queue:
        d, u = heapq.heappop(h_queue)
        if dist[u] < d:
            continue
        for to, w in adj[u]:
            if dist[to] > dist[u] + w:
                dist[to] = dist[u] + w
                heapq.heappush(h_queue, (dist[to], to))
    max_wait = max(dist[1:])
    return -1 if max_wait == float('inf') else max_wait


# 另一种写法，来自 solution
def _solve1(times, N, K):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    pq = [(0, K)]
    dist = {}
    while pq:
        d, node = heapq.heappop(pq)
        if node in dist:
            continue
        dist[node] = d
        for nei, d2 in graph[node]:
            if nei not in dist:
                heapq.heappush(pq, (d + d2, nei))

    return max(dist.values()) if len(dist) == N else -1


# Bellman-Ford：会超时
def _solve2(times, N, K):
    dist = [float('inf')] * (N + 1)
    dist[K] = 0
    for _ in xrange(N):
        for u, v, w in times:
            if dist[u] != float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
    max_wait = max(dist[1:])
    return -1 if max_wait == float('inf') else max_wait


# 改进后的想法：SPFA
def _solve3(times, N, K):
    graph = collections.defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist, visited = [float('inf')] * (N + 1), [False] * (N + 1)
    dist[K], visited[K] = 0, True
    queue = collections.deque()
    queue.append(K)

    while queue:
        u = queue.popleft()
        visited[u] = False

        for v, w in graph[u]:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if not visited[v]:
                    queue.append(v)

    max_wait = max(dist[1:])
    return -1 if max_wait == float('inf') else max_wait
