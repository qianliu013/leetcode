# coding=utf-8

"""Game of Life.

>>> solve = _solve
>>> board = [[1, 1, 0, 1], [0, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 0]]
>>> solve(board)
>>> board == [[1, 1, 0, 1], [0, 0, 0, 1], [1, 0, 0, 1], [1, 1, 0, 0]]
True
"""


# 此题的 Infinite board solution 请见：https://discuss.leetcode.com/topic/26236/infinite-board-solution
def _solve(board):
    width, height = len(board[0]), len(board)
    for i in xrange(height):
        for j in xrange(width):
            live = 0
            for inc_i in [-1, 0, 1]:
                for inc_j in [-1, 0, 1]:
                    if 0 <= i + inc_i < height and 0 <= j + inc_j < width:
                        live += board[i + inc_i][j + inc_j] & 1
            live -= board[i][j] & 1
            if board[i][j] == 1 and 2 <= live <= 3:
                board[i][j] = 3
            if board[i][j] == 0 and live == 3:
                board[i][j] = 2
    for i in xrange(height):
        for j in xrange(width):
            board[i][j] >>= 1
