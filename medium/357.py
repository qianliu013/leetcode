# coding=utf-8

"""Count Numbers with Unique Digits.

>>> solve = _solve
>>> [_solve(i) for i in range(7)]
[1, 10, 91, 739, 5275, 32491, 168571]
"""


# 简单的数学题
def _solve(n):
    digits = [9, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ans, product = 1, 1
    for i in range(min(n, 10)):
        product *= digits[i]
        ans += product
    return ans
