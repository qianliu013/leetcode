# coding=utf-8
"""Populating Next Right Pointers in Each Node II.

>>> solve = _solve
"""


# Definition for binary tree with next pointer.
class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def _solve(root):
    prev_layer, faker = root, TreeLinkNode(-1)
    while prev_layer:
        prev = faker
        while prev_layer:
            if prev_layer.left:
                prev.next = prev_layer.left
                prev = prev.next
            if prev_layer.right:
                prev.next = prev_layer.right
                prev = prev.next
            prev_layer = prev_layer.next
        prev_layer, faker.next = faker.next, None
