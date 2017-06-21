# coding=utf-8

""" Merge Two Binary Trees."""

from __future__ import print_function
from TreeNode import TreeNode


def _solve(t1, t2):
    def _help(t1, t2):
        t1.val += t2.val
        if t1.left and t2.left:
            _help(t1.left, t2.left)
        if t1.right and t2.right:
            _help(t1.right, t2.right)
        if not t1.left:
            t1.left = t2.left
        if not t1.right:
            t1.right = t2.right
        return t1
    if t1 and t2:
        return _help(t1, t2)
    if t1 and not t2:
        return t1
    if t2 and not t1:
        return t2
    return None


def _solve1(t1, t2):
    def _help(t1, t2):
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = _help(t1.left, t2.left)
        t1.right = _help(t1.right, t2.right)
        return t1
    return _help(t1, t2)


if __name__ == '__main__':
    print (_solve1(None, None))
    _solve1(TreeNode.de_serialize('[1,3,2,5]'), None).print_tree()
    _solve1(None, TreeNode.de_serialize('[2,1,3,null,4,null,7]')).print_tree()
    _solve1(TreeNode.de_serialize('[1,3,2,5]'), TreeNode.de_serialize('[2,1,3,null,4,null,7]')).print_tree()
    _solve1(TreeNode.de_serialize('[2,1,3,null,4,null,7]'), TreeNode.de_serialize('[1,3,2,5]')).print_tree()
