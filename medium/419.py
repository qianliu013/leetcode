# coding=utf-8

"""Battleships in a Board."""

from __future__ import print_function


def _solve(board):
    ans = 0
    width, height = len(board[0]), len(board)
    for row_i, row in enumerate(board):
        for column_i, entity in enumerate(row):
            if entity == 'X':
                if ((row_i + 1 == height or board[row_i + 1][column_i] == '.')
                        and (column_i + 1 == width or board[row_i][column_i + 1] == '.')):
                    ans += 1
    return ans


if __name__ == '__main__':
    BOARD = ["X..X", ".X.X", "X..X"]
    print (_solve(BOARD))
    BOARD = ["X...X", "X.X.X", "X...X"]
    print (_solve(BOARD))
    BOARD = ["XXX"]
    print (_solve(BOARD))
