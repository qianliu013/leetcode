# coding=utf-8

"""Rotate Image.

>>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> solve = _solve
>>> solve(matrix)
>>> matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
True
"""


# 从最外面一层逐步到里面
def _solve(matrix):
    start, end = 0, len(matrix) - 1
    while start < end:
        for i in xrange(end - start):
            matrix[start + i][end], matrix[end][end - i], matrix[end - i][start], matrix[start][start + i] =\
                matrix[start][start + i], matrix[start + i][end], matrix[end][end - i], matrix[end - i][start]
        start += 1
        end -= 1


# 其他写法：翻转+转置，两种：整个矩阵翻转+转置（下面代码）；转置+矩阵的每一行翻转
# 代码参考自：https://discuss.leetcode.com/topic/6796/a-common-method-to-rotate-the-image
def _solve1(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


# 以下两种及更多实现代码可参考：https://discuss.leetcode.com/topic/15295/seven-short-solutions-1-to-7-lines
def _solve2(matrix):
    matrix[:] = zip(*matrix[::-1])  # or: matrix[:] = map(list, zip(*matrix[::-1]))


# 直接的四分之一矩阵元素替换
def _solve3(matrix):
    n = len(matrix)
    for i in range(n / 2):
        for j in range(n - n / 2):
            matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                matrix[~j][i], matrix[~i][~j], matrix[j][~i], matrix[i][j]
