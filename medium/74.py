# coding=utf-8
"""Search a 2D Matrix.

>>> solve = _solve
>>> solve([], 0)
False
>>> solve([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
True
"""


# 也可以先按行二分，在按列二分，时间复杂度均是，O(log(n) + log(m))
def _solve(matrix, target):
    if not matrix or not matrix[0]:
        return False
    n = len(matrix[0])
    low, high = 0, n * len(matrix)
    while low < high:
        mid = (low + high) / 2
        cur = matrix[mid / n][mid % n]
        if cur == target:
            return True
        elif cur < target:
            low = mid + 1
        else:
            high = mid
    return False
