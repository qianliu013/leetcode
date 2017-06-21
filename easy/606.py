# coding=utf-8

"""Construct String from Binary Tree."""

from __future__ import print_function
from TreeNode import TreeNode


def _solve(t):
    def _help(t):
        ans = str(t.val)
        if t.left and t.right:
            return ans + '(' + _help(t.left) + ')' + '(' + _help(t.right) + ')'
        if not t.left and t.right:
            return ans + '()' + '(' + _help(t.right) + ')'
        if t.left and not t.right:
            return ans + '(' + _help(t.left) + ')'
        if not t.left and not t.right:
            return ans
    return _help(t) if t else ''


if __name__ == '__main__':
    print (_solve(None))
    print (_solve(TreeNode.de_serialize('[1,2,3,4]')))
    print (_solve(TreeNode.de_serialize('[1,2,3,null,4]')))
