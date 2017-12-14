# coding=utf-8

"""Gray Code.

>>> solve = _solve
>>> solve(0)
[0]
>>> solve(3)
[0, 1, 3, 2, 6, 7, 5, 4]
"""


def _solve(n):
    res, step = [0], 1
    for _ in xrange(n):
        res.extend([num | step for num in res[::-1]])
        step <<= 1
    return res


# 解释可见： https://discuss.leetcode.com/topic/8557/an-accepted-three-line-solution-in-java
def _solve1(n):
    return [(i >> 1) ^ i for i in xrange(2**n)]
