# coding=utf-8

"""Find Bottom Left Tree Value."""

from __future__ import print_function
from TreeNode import TreeNode


# DFS 1
def _solve(root):
    def _help(root, depth):
        if not root.left and not root.right:
            return root.val, depth
        if root.left and root.right:
            left_ans = _help(root.left, depth + 1)
            right_ans = _help(root.right, depth + 1)
            return right_ans if left_ans[1] < right_ans[1] else left_ans
        return _help(root.left or root.right, depth + 1)

    return _help(root, 0)[0] if root else 0


# DFS2, fastest, 59 ms, beats 99.14%
def _solve1(root):
    def _help(root, depth, result):
        if result[1] < depth:
            result[:] = [root.val, depth]
        if root.left:
            _help(root.left, depth + 1, result)
        if root.right:
            _help(root.right, depth + 1, result)
        return result[0]
    return _help(root, 1, [0, 0])


# BFS with tricks
def _solve2(root):
    queue = [root]
    for node in queue:
        queue += filter(None, (node.right, node.left))
    return node.val


# BFS in python
def _solve3(root):
    queue, ans = [root], 0
    while any(queue):
        ans = queue[0].val
        queue = [leaf for node in queue for leaf in (node.left, node.right) if leaf]
    return ans


if __name__ == '__main__':
    print (_solve3(TreeNode.de_serialize('[2]')))
    print (_solve3(TreeNode.de_serialize('[2,1,3]')))
    print (_solve3(TreeNode.de_serialize('[1,2,3,4,null,5,6,null,null,7]')))
