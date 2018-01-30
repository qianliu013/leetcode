# coding=utf-8
"""Bitwise AND of Numbers Range.

>>> solve = _solve2
>>> solve(5, 7)
4
"""


# 从左到右
def _solve(m, n):
    for i in xrange(31, -1, -1):
        cur = 1 << i
        if m & cur != n & cur:
            break
    return m & (0xffffffff << i)


# 从右到左
def _solve1(m, n):
    step = 0
    while m != n:
        m >>= 1
        n >>= 1
        step += 1
    return m << step


# 代码来自：https://discuss.leetcode.com/topic/20176/2-line-solution-with-detailed-explanation/5
# 解释（来自评论）
# given m < n
# m := common bits + 0 + remaining bits of m
# n := common bits + 1 + remaining bits of n.
# thus repeatedly clear last bit of n, until n <= m
def _solve2(m, n):
    while m < n:
        n &= n - 1
    return n
