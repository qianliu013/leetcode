# coding=utf-8

"""Valid Square.

>>> solve = _solve
>>> solve([0, 0], [1, 1], [1, 0], [0, 1])
True
"""


# 正方形只要判断 4条边长度相等 + 2条对角线长度相等 即可，无需判断垂直，因此代码相对简单
# 四个点构成四边形其实就三种情况，逐一判断即可
def _solve(p1, p2, p3, p4):
    def _dist(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    paths = [[p1, p2, p3, p4], [p1, p2, p4, p3], [p1, p3, p2, p4]]
    for path in paths:
        edges = [_dist(path[i], path[i - 1]) for i in xrange(4)]
        if edges[0] == edges[1] == edges[2] == edges[3] != 0 and _dist(path[0], path[2]) == _dist(path[1], path[3]):
            return True
    return False


# 排序确定四个点的位置也可以
def _solve1(p1, p2, p3, p4):
    def _dist(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    path = sorted([p1, p2, p3, p4])
    return _dist(path[0], path[1]) == _dist(path[0], path[2]) == _dist(path[1], path[3]) == _dist(path[2], path[3]) != 0 and _dist(path[0], path[3]) == _dist(path[1], path[2])


# 下面这种简洁的代码只能用于边长为整数的情况
# 相关讨论请见：https://discuss.leetcode.com/topic/89985/c-3-lines-unordered_set
def _solve2(p1, p2, p3, p4):
    def _dist(p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    res = {_dist(p1, p2), _dist(p1, p3), _dist(p1, p4), _dist(p2, p3), _dist(p2, p4), _dist(p3, p4)}
    return len(res) == 2 and 0 not in res
