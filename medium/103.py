# coding=utf-8
"""Binary Tree Zigzag Level Order Traversal.

>>> solve = _solve
"""

from TreeNode import TreeNode


def _solve(root):
    if not root:
        return []
    step, queue, ans = 1, [root], []
    while queue:
        ans.append([node.val for node in queue[::step]])
        queue = [kid for node in queue for kid in (node.left, node.right) if kid]
        step *= -1
    return ans


assert _solve(TreeNode.de_serialize('[3,9,20,null,null,15,7]')) == [[3], [20, 9], [15, 7]]
