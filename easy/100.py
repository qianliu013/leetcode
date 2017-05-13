# coding=utf-8

"""Same Tree."""

from __future__ import print_function


def _solve(p, q):
    def is_equal(tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 and tree2:
            if tree1.val == tree2.val:
                return is_equal(tree1.left, tree2.left) and \
                    is_equal(tree1.right, tree2.right)

        return False

    return is_equal(p, q)
