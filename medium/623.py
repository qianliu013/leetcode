# coding=utf-8

"""Add One Row to Tree."""

from TreeNode import TreeNode


# dfs
def _solve(root, v, d):
    def _dfs(root, depth):
        if root:
            if depth == 0:
                new_left = TreeNode(v)
                new_right = TreeNode(v)
                new_left.left = root.left
                new_right.right = root.right
                root.left = new_left
                root.right = new_right
                return
            _dfs(root.left, depth - 1)
            _dfs(root.right, depth - 1)

    if d == 1:
        new_root = TreeNode(v)
        new_root.left = root
        return new_root
    _dfs(root, d - 1)
    return root


# bfs，参考 https://discuss.leetcode.com/topic/92938/short-python-bfs
def _solve1(root, v, d):
    dummy, dummy.left = TreeNode(None), root
    row = [dummy]
    for _ in xrange(d - 1):
        row = [kid for node in row for kid in (node.left, node.right) if kid]
    for node in row:
        node.left, node.left.left = TreeNode(v), node.left
        node.right, node.right.right = TreeNode(v), node.right
    return dummy.left
