# coding=utf-8

"""Monotone Increasing Digits.

>>> solve = _solve
>>> _solve(110)
99
>>> _solve(120)
119
"""


# 一种思路是只要找到前一位比后一位大的数，那么之后的全部置9；需要特殊考虑的就是相等的情况
def _solve(N):
    digits, marker = str(N), -1
    for i in xrange(len(digits) - 1, 0, -1):
        if digits[i - 1] > digits[i] or (marker != -1 and digits[marker] == digits[i - 1]):
            marker = i - 1
    return N if marker == -1 else N - int(digits[marker + 1:]) - 1


# 另一种是从低位到高位，遇到比低位小的数，则前一位减 1，并记录；最后记录位后的数全部置 9
# 代码参考自： https://discuss.leetcode.com/topic/112826/simple-and-very-short-c-solution
def _solve1(N):
    digits = map(int, str(N))
    marker = len(digits)
    for i in xrange(len(digits) - 1, 0, -1):
        if digits[i] < digits[i - 1]:
            marker = i
            digits[i - 1] -= 1
    for i in xrange(marker, len(digits)):
        digits[i] = 9
    return int(''.join(map(str, digits)))
