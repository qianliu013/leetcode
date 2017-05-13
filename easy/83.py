# coding=utf-8

"""Remove Duplicates from Sorted List."""

from __future__ import print_function
from ListNode import ListNode


def _solve(head):
    if not head or not head.next:
        return head
    prev_node = head
    next_node = head
    while next_node.next:
        next_node = next_node.next
        if prev_node.val != next_node.val:
            prev_node.next = next_node
            prev_node = next_node
    prev_node.next = next_node.next
    return head


if __name__ == '__main__':
    NODE_LIST = ListNode.from_list([1, 2, 1, 1, 1])
    NODE_LIST.print_list()
    _solve(NODE_LIST).print_list()
