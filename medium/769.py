# coding=utf-8
"""Max Chunks To Make Sorted.

>>> solve = _solve
>>> solve([4, 3, 2, 1, 0])
1
>>> solve([1, 0, 2, 3, 4])
4
"""


# 更多思路可参考：hard/769 Max Chunks To Make Sorted II.
def _solve(arr):
    ans = max_i = 0
    for i, num in enumerate(arr):
        max_i = max(max_i, num)
        if max_i == i:
            ans += 1
    return ans
