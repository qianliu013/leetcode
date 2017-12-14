# coding=utf-8

"""Flood Fill.

>>> solve = _solve
>>> _solve([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
[[2, 2, 2], [2, 2, 0], [2, 0, 1]]
"""


def _solve(image, sr, sc, newColor):
    color, width, height = image[sr][sc], len(image[0]), len(image)
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def _floor(row, col):
        if image[row][col] == color:
            image[row][col] = newColor
            for i, j in dirs:
                if 0 <= row + i < height and 0 <= col + j < width:
                    _floor(row + i, col + j)

    if newColor != color:
        _floor(sr, sc)
    return image
