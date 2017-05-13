# coding=utf-8

"""Diameter of Binary Tree."""

from __future__ import print_function
from TreeNode import TreeNode


def _solve(root):
    result = {
        'max_dis': 0
    }

    def _deep(cur):
        if cur:
            max_left = _deep(cur.left) + 1
            max_right = _deep(cur.right) + 1
            result['max_dis'] = max(result['max_dis'], max_left + max_right)
            return max(max_left, max_right)
        else:
            return -1

    _deep(root)
    return result['max_dis']


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    print (_solve(node1))
