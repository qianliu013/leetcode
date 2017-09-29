# coding=utf-8

"""Trim a Binary Search Tree.

>>> solve = _solve
>>> solve(TreeNode.de_serialize('[1,0,2]'), 1, 2).print_tree()
1 -> 2 
>>> solve(TreeNode.de_serialize('[3,0,4,null,2,null,null,1,null]'), 1, 3).print_tree()
3 -> 2 -> 1 
"""

from TreeNode import TreeNode


def _solve(root, L, R):
    def _dfs(node):
        if not node:
            return None
        if node.val < L:
            return _dfs(node.right)
        if node.val > R:
            return _dfs(node.left)
        node.left = _dfs(node.left)
        node.right = _dfs(node.right)
        return node

    return _dfs(root)
