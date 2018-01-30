# coding=utf-8

"""Sum Root to Leaf Numbers.

>>> solve = _solve
"""


def _solve(root):
    def _dfs(cur, num):
        if not cur:
            return 0
        res = num * 10 + cur.val
        if not cur.left and not cur.right:
            return res
        return _dfs(cur.left, res) + _dfs(cur.right, res)

    return _dfs(root, 0)
