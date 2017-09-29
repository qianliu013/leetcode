# coding=utf-8

"""Second Minimum Node In a Binary Tree.

>>> solve = _solve1
>>> solve(TreeNode.de_serialize('[2,2,5,null,null,5,7]'))
5
>>> solve(TreeNode.de_serialize('[2,2,2]'))
-1
"""


def _solve(root):
    res = [-1, -1]

    def _dfs(node):
        if node:
            if res[0] == -1 or res[0] > node.val:
                res[0] = node.val
            elif res[0] != node.val and (res[1] > node.val or res[1] == -1):
                res[1] = node.val
            _dfs(node.left)
            _dfs(node.right)

    _dfs(root)
    return res[1]


def _solve1(root):
    res = [root.val, float('inf')]

    def _dfs(node):
        if node:
            if res[0] < node.val < res[1]:
                res[1] = node.val
            else:
                _dfs(node.left)
                _dfs(node.right)
    _dfs(root)
    return res[1] if res[1] != float('inf') else -1
