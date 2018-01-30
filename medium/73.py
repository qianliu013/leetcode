# coding=utf-8

"""Set Matrix Zeroes.

>>> solve = _solve
"""


# 思路是使用第一行、第一列的每个元素是否为 0 表示该列、该行是否置0
# 然后用额外的两个值来表示第一列第一行是否置0
# 但是也可以通过按序访问的缘故，只保存一个值即可
# 下面是我最初的想法
def _solve(matrix):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return
    row0 = 1
    for num in matrix[0]:
        if num == 0:
            row0 = 0
            break
    for row in matrix[1:]:
        cur_row = 1
        for j, num in enumerate(row):
            if num == 0:
                cur_row = 0
                matrix[0][j] = 0
        if cur_row == 0:
            for j, _ in enumerate(row):
                row[j] = 0
    for j, num in enumerate(matrix[0]):
        if num == 0:
            for i in xrange(len(matrix)):
                matrix[i][j] = 0
    if row0 == 0:
        for j, _ in enumerate(matrix[0]):
            matrix[0][j] = 0


# 一种简洁的写法
# 代码参考自：https://leetcode.com/problems/set-matrix-zeroes/discuss/26014/
def _solve1(matrix):
    col0, rows, cols = 1, len(matrix), len(matrix[0])
    for i in xrange(rows):
        if matrix[i][0] == 0:
            col0 = 0
        for j in xrange(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in xrange(rows - 1, -1, -1):
        for j in xrange(cols - 1, 0, -1):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
        if col0 == 0:
            matrix[i][0] = 0
