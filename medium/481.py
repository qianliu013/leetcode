# coding=utf-8

"""Magical String.

>>> solve = _solve
>>> solve(6)
3
"""


# 构造原有数组
def _solve(n):
    chars, cur_i = [1, 2, 2], 2
    while len(chars) < n:
        chars.extend([3 ^ chars[-1]] * chars[cur_i])
        cur_i += 1
    return chars[:n].count(1)


# 有种 O(log n) 空间的做法，可参考 
# https://discuss.leetcode.com/topic/75242/o-log-n-space-using-recursive-generators