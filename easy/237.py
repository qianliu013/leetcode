# coding=utf-8

"""Delete Node in a Linked List."""

from __future__ import print_function
from ListNode import ListNode


def _solve(node):
    node.val = node.next.val
    node.next = node.next.next


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    _solve(node3)
    node1.print_list()
