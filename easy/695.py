# coding=utf-8

"""Max Area of Island.

>>> solve = _solve
>>> solve([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])
6
"""


def _solve(grid):
    width, height = len(grid[0]), len(grid)
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * width for _ in xrange(height)]

    def _dfs(row, col):
        if -1 < row < height and -1 < col < width and not visited[row][col] and grid[row][col]:
            visited[row][col] = True
            return sum([_dfs(row + row_c, col + col_c) for row_c, col_c in dirs]) + 1
        else:
            return 0

    return max(_dfs(row, col) for row in xrange(height) for col in xrange(width))
