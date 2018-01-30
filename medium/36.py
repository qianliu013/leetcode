# coding=utf-8

"""Valid Sudoku.

>>> solve = _solve
"""


# 此题只使用一个 set 的方法（非通过行、列等遍历重新生成 set）是编码
# 在 python 中可以用 tuple 实现这一点，其实也可以将行、列、第几块编码形成独一无二的字符串
# 具体可参考 https://discuss.leetcode.com/topic/27436/short-simple-java-using-strings
def _solve(board):
    sets = [0 for _ in xrange(9)]
    row_sets, col_sets, sub_sets = list(sets), list(sets), list(sets)
    for i in xrange(9):
        for j in xrange(9):
            if board[i][j] != '.':
                num = 1 << (int(board[i][j]) - 1)
                nth = i / 3 * 3 + j / 3
                if row_sets[i] & num or col_sets[j] & num or sub_sets[nth] & num:
                    return False
                row_sets[i] |= num
                col_sets[j] |= num
                sub_sets[nth] |= num
    return True
