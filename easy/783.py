# coding=utf-8
"""Minimum Distance Between BST Nodes."""


def _solve(root):
    res = [float('-inf'), float('inf')]

    def _inorder(node):
        if node:
            _inorder(node.left)
            res[1] = min(res[1], node.val - res[0])
            res[0] = node.val
            _inorder(node.right)

    _inorder(root)
    return res[1]
