# coding=utf-8

"""Symmetric Tree."""

from __future__ import print_function
from TreeNode import TreeNode


def _solve(root):
    queue = [root, root]
    while len(queue):
        node_left = queue.pop(0)
        node_right = queue.pop(0)
        if node_left and node_right:
            if node_left.val != node_right.val:
                return False
            else:
                queue.extend((node_left.left, node_right.right,
                              node_left.right, node_right.left))
        if node_left and not node_right:
            return False
        if not node_left and node_right:
            return False
    return True


def _solve1(root):
    def _help(left, right):
        if not left and not right:
            return True
        if None in (left, right):
            return False
        return left.val == right.val and\
            _help(left.left, right.right) and _help(left.right, right.left)

    return _help(root.left, root.right) if root else True


if __name__ == '__main__':
    symmetric_tree = TreeNode.de_serialize('[1,2,2,3,4,4,3]')
    print (_solve1(symmetric_tree))
    no_symmetric_tree = TreeNode.de_serialize('[1,2,2,null,3,null,3]')
    print (_solve1(no_symmetric_tree))
    no_symmetric_tree = TreeNode.de_serialize('[1,2,2,3,null,3,null]')
    print (_solve1(no_symmetric_tree))
    no_symmetric_tree = TreeNode.de_serialize('[1,2,2,4,null,null,3]')
    print (_solve1(no_symmetric_tree))
    print (_solve1(TreeNode(1)))
    print (_solve1(None))
