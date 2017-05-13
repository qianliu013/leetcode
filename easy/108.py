# coding=utf-8

"""convert Sorted Array to Binary Search Tree."""

from __future__ import print_function
from TreeNode import TreeNode


def _solve(nums):
    def _deep(left, right):
        mid = (left + right) / 2
        mid_node = TreeNode(nums[mid])
        if left < mid:
            mid_node.left = _deep(left, mid - 1)
        if right > mid:
            mid_node.right = _deep(mid + 1, right)
        return mid_node

    return _deep(0, len(nums) - 1) if len(nums) else None


if __name__ == '__main__':
    root = _solve([1, 3, 4, 7])
    root.print_tree_in_order()
    print (root.get_depth())
