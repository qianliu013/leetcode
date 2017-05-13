# coding=utf-8

"""Balanced Binary Tree."""

from TreeNode import TreeNode


def _solve(root):
    ans = [True]

    def _help(root):
        if not root:
            return 0
        if root:
            left_depth = _help(root.left)
            right_depth = _help(root.right)
            if abs(left_depth - right_depth) > 1:
                ans[0] = False
            return max(left_depth, right_depth) + 1

    _help(root)
    return ans[0]


if __name__ == '__main__':
    ROOT = None
    print _solve(ROOT)
    ROOT = TreeNode.de_serialize('[1]')
    print _solve(ROOT)
    ROOT = TreeNode.de_serialize('[1,2,null]')
    print _solve(ROOT)
    ROOT = TreeNode.de_serialize('[1,2,null,1]')
    print _solve(ROOT)
