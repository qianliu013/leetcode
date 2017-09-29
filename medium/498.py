# coding=utf-8

"""Diagonal Traverse.

>>> solve = _solve1
>>> solve([])
[]
>>> solve([[1, 2], [1, 2], [1, 2]])
[1, 2, 1, 1, 2, 2]
>>> solve([[1, 2, 3], [1, 2, 3]])
[1, 2, 1, 2, 3, 3]
>>> solve([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
[1, 2, 1, 1, 2, 3, 3, 2, 3]
"""


# 直接模拟、迭代顺序、处理边界的方法可参考
# https://discuss.leetcode.com/topic/77865/concise-java-solution/19

# 0 - (n-1) 元素分别向右移动 0 - (n-1)，记录输出
def _solve(matrix):
    if not matrix:
        return []
    i, j, i_inc = 0, 0, -1
    width, height = len(matrix[0]), len(matrix)
    ans = []
    processed = False
    while j < width + height:
        processed = False
        while i >= 0 and i < height:
            if i <= j and j - i < width:
                ans.append(matrix[i][j - i])
                processed = True
            elif processed:
                i += i_inc
                break
            i += i_inc
        j += 1
        i_inc *= -1
        i += i_inc
    return ans


# 处理所有对角线元素：写法很多，如：
def _solve1(matrix):
    row, col, width, height = 0, 0, len(matrix and matrix[0]), len(matrix)
    ans = [None] * width * height
    for i in range(height * width):
        ans[i] = matrix[row][col]
        if (row + col) % 2 == 0:
            if col == width - 1:
                row += 1
            elif row == 0:
                col += 1
            else:
                row -= 1
                col += 1
        else:
            if row == height - 1:
                col += 1
            elif col == 0:
                row += 1
            else:
                row += 1
                col -= 1
    return ans


# 极简写法，参考 https://discuss.leetcode.com/topic/77933/sorting-and-normal-python
# 上述连接中还有种方法，即通过依次判断每条对角线(共 width + height - 1 条）的方向与数量并直接填入数组
def _solve2(matrix):
    entries = [(i + j, (j, i)[(i ^ j) & 1], val)
               for i, row in enumerate(matrix)
               for j, val in enumerate(row)]
    return [e[2] for e in sorted(entries)]


# 这种写法思路会简单、明确很多
# https://discuss.leetcode.com/topic/78345/python-solution-with-detailed-explanation-deque
