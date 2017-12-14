# coding=utf-8

"""Binary Tree Level Order Traversal."""


def _solve(root):
    if not root:
        return []
    res, layer = [], [root]
    while layer:
        res.append([node.val for node in layer])
        layer = [child for node in layer for child in (node.left, node.right) if child]
    return res
