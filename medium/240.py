# coding=utf-8

"""Search a 2D Matrix II.

>>> solve = _solve
>>> solve([], 1)
False
>>> solve([[]], 1)
False
>>> solve([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5)
True
>>> solve([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20)
False
"""


def _solve(matrix, target):
    if not matrix or not matrix[0]:
        return False
    j = len(matrix[0])
    for i in xrange(len(matrix)):
        while j > 0 and matrix[i][j - 1] > target:
            j -= 1
        if matrix[i][j - 1] == target:
            return True
    return False


# 常见的只用一个 while 的写法
def _solve1(matrix, target):
    if not matrix or not matrix[0]:
        return False
    height, width = len(matrix), len(matrix[0])
    i, j = 0, width - 1
    while i < height and j >= 0:
        if matrix[i][j] == target:
            return True
        if matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False
