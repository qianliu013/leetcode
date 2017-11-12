# coding=utf-8

"""1-bit and 2-bit Characters.

>>> solve = _solve
>>> solve([1, 0, 0])
True
>>> solve([1, 1, 1, 0])
False
"""


def _solve(bits):
    i, length = 0, len(bits)
    while i < length - 1:
        i += bits[i] + 1
    return i == length - 1


# 参考自该题的 solution，https://leetcode.com/articles/1-bit-and-2-bit-characters/
def _solve1(bits):
    i = len(bits) - 2
    while i >= 0 and bits[i] > 0:
        i -= 1
    return (len(bits) - i) % 2 == 0
