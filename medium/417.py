# coding=utf-8
"""Pacific Atlantic Water Flow.

>>> solve = _solve
>>> solve([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]])
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
>>> solve([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
[[0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
"""


def _solve(matrix):
    if not matrix or not matrix[0]:
        return []
    height, width = len(matrix), len(matrix[0])
    pacific, atlantic = [[False] * width for _ in xrange(height)], [[False] * width for _ in xrange(height)]

    def _search(ocean, stack):
        while stack:
            x, y = stack.pop()
            if not ocean[x][y]:
                ocean[x][y] = True
                for x_inc, y_inc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if (0 <= x + x_inc < height and 0 <= y + y_inc < width
                            and matrix[x + x_inc][y + y_inc] >= matrix[x][y]):
                        stack.append((x + x_inc, y + y_inc))

    _search(pacific, [(i, 0) for i in xrange(height)] + [(0, j) for j in xrange(width)])
    _search(atlantic, [(i, width - 1) for i in xrange(height)] + [(height - 1, j) for j in xrange(width)])
    return [[i, j] for i in xrange(height) for j in xrange(width) if pacific[i][j] and atlantic[i][j]]
