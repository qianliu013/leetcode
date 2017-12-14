# coding=utf-8

"""Spiral Matrix II.

>>> solve = _solve
>>> solve(4)
[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
"""


# 单步走
def _solve(n):
    res = [[0] * n for _ in xrange(n)]
    i, x, y = 1, 0, 0
    cur, dirs = 0, [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for i in xrange(1, n * n + 1):
        res[x][y] = i
        next_x, next_y = x + dirs[cur][0], y + dirs[cur][1]
        if 0 <= next_x < n and 0 <= next_y < n and res[next_x][next_y] == 0:
            i += 1
            x, y = next_x, next_y
        else:
            cur = (cur + 1) % 4
            x, y = x + dirs[cur][0], y + dirs[cur][1]
    return res


# 四步走
def _solve1(n):
    res = [[0] * n for _ in xrange(n)]
    left, top, right, down = 0, 0, n - 1, n - 1
    count = 1
    while left <= right:
        for j in xrange(left, right + 1):
            res[top][j] = count
            count += 1
        top += 1
        for i in xrange(top, down + 1):
            res[i][right] = count
            count += 1
        right -= 1
        for j in xrange(right, left - 1, -1):
            res[down][j] = count
            count += 1
        down -= 1
        for i in xrange(down, top - 1, -1):
            res[i][left] = count
            count += 1
        left += 1
    return res

# 此外，还有两种十分巧妙地方法，可以参考
# https://discuss.leetcode.com/topic/19130/4-9-lines-python-solutions
