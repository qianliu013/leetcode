# coding=utf-8

"""Most Frequent Subtree Sum.

>>> from TreeNode import TreeNode
>>> solve = _solve
>>> solve(TreeNode.de_serialize('[5,2,-3]')) == [2, 4, -3]
True
>>> solve(TreeNode.de_serialize('[5,2,-5]')) == [2]
True
"""


def _solve(root):
    if not root:
        return []
    result = {}

    def _deep(node):
        if node:
            sub_sum = _deep(node.left) + _deep(node.right) + node.val
            result[sub_sum] = result.get(sub_sum, 0) + 1
            return sub_sum
        else:
            return 0
    _deep(root)
    frequent_sum_total = max(result.values())
    return [node_sum for node_sum, num in result.items() if num == frequent_sum_total]
