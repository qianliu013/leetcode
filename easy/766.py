# coding=utf-8
"""Toeplitz Matrix.

>>> solve = _solve
>>> solve([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]])
True
>>> solve([[1, 2], [2, 2]])
False
"""


def _solve(matrix):
    height, width = len(matrix), len(matrix[0])
    diagonals = [None] * (height + width)
    for i in xrange(height):
        for j in xrange(width):
            nth = height - 1 - i + j
            if diagonals[nth] and diagonals[nth] != matrix[i][j]:
                return False
            diagonals[nth] = matrix[i][j]
    return True


# 另一种十分巧妙的思路，来自 Solution
def _solve1(matrix):
    return all(
        r == 0 or c == 0 or matrix[r - 1][c - 1] == val for r, row in enumerate(matrix) for c, val in enumerate(row))
