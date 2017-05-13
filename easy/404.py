# coding=utf-8

"""Sum of Left Leaves."""

from __future__ import print_function
from TreeNode import TreeNode


def _sum_of_left_leaves(root):
    _is_left = True

    def _solve(cur, is_left):
        if not cur:
            return 0
        if cur.left is None and cur.right is None:
            if is_left:
                return cur.val
            else:
                return 0
        return _solve(cur.left, _is_left) + _solve(cur.right, not _is_left)

    return _solve(root, not _is_left)

if __name__ == '__main__':
    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node3.left = node9
    node3.right = node20
    node20.left = node15
    node20.right = node7
    print (_sum_of_left_leaves(node3))
    print (_sum_of_left_leaves(TreeNode(1)))
