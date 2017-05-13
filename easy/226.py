# coding=utf-8

"""Invert Binary Tree."""

from TreeNode import TreeNode


def _invert_tree(root):
    if root:
        # 下面三行可以写成一行
        root.left, root.right = root.right, root.left
        _invert_tree(root.left)
        _invert_tree(root.right)
    return root


if __name__ == '__main__':
    node4 = TreeNode(4)
    node7 = TreeNode(7)
    node2 = TreeNode(2)
    node9 = TreeNode(9)
    node6 = TreeNode(6)
    node3 = TreeNode(3)
    node1 = TreeNode(1)
    node4.left = node2
    node4.right = node7
    node2.left = node1
    node2.right = node3
    node7.left = node6
    node7.right = node9
    node4.print_tree()
    print ('========')
    _invert_tree(node4).print_tree()
