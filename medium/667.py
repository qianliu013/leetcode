# coding=utf-8

"""Beautiful Arrangement II.

>>> solve = _solve
>>> solve(3,2)
[1, 3, 2]
"""


# 找规律，构造数列
def _solve(n, k):
    ans, flag = range(1, n + 1), 1
    for diff in range(k, 0, -1):
        index = n - diff
        ans[index] = ans[index - 1] + flag * diff
        flag *= -1
    return ans
