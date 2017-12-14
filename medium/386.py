# coding=utf-8

"""Lexicographical Numbers.

>>> solve = _solve1
>>> solve(13)
[1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
"""


def _solve(n):
    res = []

    i = 1
    while len(res) != n:
        while i <= n:
            res.append(i)
            i *= 10
        i = res[-1] + 1
        while i % 10 != 0:
            if i <= n:
                res.append(i)
            i += 1
        while i % 10 == 0:
            i /= 10
    return res


# 参考自
# https://discuss.leetcode.com/topic/55131/ac-200ms-c-solution-beats-98
# 另一种简洁写法可以参考
# https://discuss.leetcode.com/topic/56467/the-most-elegant-python-solution-so-far-10-liner-iterative-o-n-time-o-1-space/2
def _solve1(n):
    cur, res = 1, []
    for _ in xrange(n):
        res.append(cur)
        if cur * 10 <= n:
            cur *= 10
        else:
            if cur >= n:
                cur /= 10
            cur += 1
            while cur % 10 == 0:
                cur /= 10
    return res


# 其他排序方式及可能存在的问题可参考
# https://discuss.leetcode.com/topic/55090/python-with-sorting
def _solve2(n):
    return sorted(range(1, n + 1), key=str)
