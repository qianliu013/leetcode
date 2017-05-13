# coding=utf-8

"""Lowest Common Ancestor of a Binary Search Tree."""

from __future__ import print_function
from TreeNode import TreeNode


def _solve(root, p, q):
    def _help(root):
        if p.val < root.val > q.val:
            return _help(root.left)
        elif p.val > root.val < q.val:
            return _help(root.right)
        return root

    return _help(root)


if __name__ == '__main__':
    root = TreeNode.de_serialize('[6,2,8,0,4,7,8,null,null,3,5]')
    print (_solve(root, TreeNode(2), TreeNode(2)).val)
    print (_solve(root, TreeNode(2), TreeNode(8)).val)
    print (_solve(root, TreeNode(7), TreeNode(9)).val)
    print (_solve(root, TreeNode(3), TreeNode(9)).val)
