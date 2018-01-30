# coding=utf-8
"""Number of Islands.

>>> solve = _solve
>>> solve([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]])
1
"""


# 可以减少比较次数从使代码运行更快
def _solve(grid):
    if not grid or not grid[0]:
        return 0
    width, height = len(grid[0]), len(grid)

    def _dfs(x, y):
        if 0 <= x < height and 0 <= y < width and grid[x][y] == '1':
            grid[x][y] = '0'
            map(_dfs, (x + 1, x - 1, x, x), (y, y, y + 1, y - 1))

    ans = 0
    for i in xrange(height):
        for j in xrange(width):
            if grid[i][j] == '1':
                _dfs(i, j)
                ans += 1
    return ans
