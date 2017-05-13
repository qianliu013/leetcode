# coding=utf-8

"""Minimum Depth of Binary Tree."""

from TreeNode import TreeNode


def _solve(root):
    def _help(root):
        if root:
            if not root.left and not root.right:
                return 1
            else:
                return min(_help(root.left), _help(root.right)) + 1
        else:
            return 1 << 30

    return _help(root) if root else 0


if __name__ == '__main__':
    print _solve(None)
    print _solve(TreeNode(1))
    print _solve(TreeNode.de_serialize('[1,23,4,5,null,5,null]'))
