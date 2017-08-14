# coding=utf-8

"""Minesweeper.

>>> solve = _solve
>>> solve(["EEEEE","EEMEE","EEEEE","EEEEE"], [1,2]) == ["EEEEE","EEXEE","EEEEE","EEEEE"]
True
>>> solve(["EEEEE","EEMEE","EEEEE","EEEEE"], [3,0]) == ["B1E1B", "B1M1B","B111B","BBBBB"]
True
"""


def _solve(board, click):
    visited = [[False] * len(row) for row in board]
    ans = [[ch for ch in row] for row in board]

    def _in_board(x, y):
        return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])

    def _adjacent_mines(x, y):
        total = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if _in_board(i + x, j + y) and board[i + x][j + y] == 'M':
                    total += 1
        return total

    def _deep(x, y):
        if visited[x][y]:
            return
        visited[x][y] = True
        mines = _adjacent_mines(x, y)
        if mines == 0:
            ans[x][y] = 'B'
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if _in_board(i + x, j + y):
                        _deep(i + x, j + y)
        else:
            ans[x][y] = str(mines)

    if board[click[0]][click[1]] == 'M':
        ans[click[0]][click[1]] = 'X'
    else:
        _deep(click[0], click[1])
    return [''.join(row) for row in ans]
