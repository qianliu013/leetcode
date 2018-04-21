# coding=utf-8
"""Water and Jug Problem.

>>> solve = _solve
>>> solve(6, 8, 14)
True
>>> solve(6, 8, 9)
False
"""

import collections


# 其实打表找规律很容易知道用 gcd 来解
# 数学解释是 [Bézout's identity](https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity)
# ax+by=d
def _solve(x, y, z):
    if x == z or y == z or x + y == z:
        return True
    if z > x + y:
        return False
    while y != 0:
        (x, y) = (y, x % y)
    return z % x == 0


# BFS 解法：TLE
def _solve1(x, y, z):
    def _next(jug1, jug2):
        return [(x, jug2), (0, jug2), (jug1 - min(jug1, y - jug2), jug2 + min(jug1, y - jug2)),
                (jug1, y), (jug1, 0), (jug1 + min(jug2, x - jug1), jug2 - min(jug2, x - jug1))]

    if x + y < z:
        return False
    visited = set()
    queue = collections.deque()
    queue.append((0, 0))
    while queue:
        cur = queue.popleft()
        if cur[0] == z or cur[1] == z or cur[0] + cur[1] == z:
            return True
        visited.add(cur)
        for nxt in _next(*cur):
            if nxt not in visited:
                queue.append(nxt)
    return False


# 改进过的 BFS 可过（虽然很慢）,代码及思路参考自：
# https://leetcode.com/problems/water-and-jug-problem/discuss/83716/Java-Programmatic-Solution-BFS-without-GCD
def _solve2(x, y, z):
    if z < 0 or z > x + y:
        return False
    visited = set()
    queue = collections.deque()
    queue.append(0)
    while queue:
        cur = queue.popleft()
        for nxt in [
                jug for jug in [cur + x, cur + y, cur - x, cur - y]
                if 0 <= jug <= x + y and jug not in visited
        ]:
            visited.add(nxt)
            queue.append(nxt)
        if z in visited:
            return True
    return False


# 此题也可以模拟来做，思路如下；参考自
# https://leetcode.com/problems/water-and-jug-problem/discuss/83727/c++-solution-follow-the-procedure
def _solve3(x, y, z):
    if x + y == z:
        return True
    if x + y < z:
        return False
    if x > y:
        x, y = y, x
    volume = 0
    while True:
        if volume < x:
            volume += y
        else:
            volume -= x
        if volume == z:
            return True
        if volume == 0:
            # 回到原点
            return False
