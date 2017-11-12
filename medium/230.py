# coding=utf-8

"""Kth Smallest Element in a BST."""
from TreeNode import TreeNode


def _solve(root, k):
    res = [0, 0]

    def _dfs(cur):
        if cur:
            _dfs(cur.left)
            res[0] += 1
            if k == res[0]:
                res[1] = cur.val
                return
            _dfs(cur.right)

    _dfs(root)
    return res[1]


def _solve1(root, k):
    def _count_nodes(cur):
        if cur:
            return 1 + _count_nodes(cur.left) + _count_nodes(cur.right)
        else:
            return 0

    def _dfs(cur, count):
        left_count = _count_nodes(cur.left)
        if count <= left_count:
            return _dfs(cur.left, count)
        elif count == left_count + 1:
            return cur.val
        else:
            return _dfs(cur.right, count - 1 - left_count)

    return _dfs(root, k)


assert [_solve1(TreeNode.de_serialize('[2,1,3]'), i) for i in xrange(1, 4)], [1, 2, 3]
