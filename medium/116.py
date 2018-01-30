# coding=utf-8

"""Populating Next Right Pointers in Each Node.

>>> solve = _solve
"""


def _solve(root):
    if root:
        prev_layer, cur_head = root, root.left
        while cur_head:
            prev_layer.left.next = prev_layer.right
            while prev_layer.next:
                prev_layer.right.next = prev_layer.next.left
                prev_layer.next.left.next = prev_layer.next.right
                prev_layer = prev_layer.next
            prev_layer, cur_head = cur_head, cur_head.left
