# coding=utf-8

"""Image Smoother."""


def _solve(M):
    dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    width, height = len(M[0]), len(M)
    res = [[0] * width for _ in xrange(height)]
    for i in xrange(height):
        for j in xrange(width):
            count, res[i][j] = 1, M[i][j]
            for x, y in dirs:
                if i + x >= 0 and i + x < height and j + y >= 0 and j + y < width:
                    res[i][j] += M[i + x][j + y]
                    count += 1
            res[i][j] /= count
    return res
