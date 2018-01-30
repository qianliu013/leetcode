# coding=utf-8
"""Rotate Function.

>>> solve = _solve
>>> solve([4, 3, 2, 6])
26
"""


def _solve(A):
    sums, f_res, length = 0, 0, len(A)
    for i, num in enumerate(A):
        f_res += i * num
        sums += num
    ans = f_res
    for i in xrange(length - 1, 0, -1):
        f_res = f_res + sums - length * A[i]
        ans = max(f_res, ans)
    return ans
