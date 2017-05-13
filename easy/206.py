# coding=utf-8

"""Reverse Linked List."""

from __future__ import print_function
from ListNode import ListNode


def _solve(head):
    prev = None
    while head:
        cur = head
        head = head.next
        cur.next = prev
        prev = cur
    return prev


def _solve1(head):
    if head is None or head.next is None:
        return head
    new_head = _solve1(head.next)
    head.next.next = head
    head.next = None
    return new_head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    print (_solve(None))
    _solve(node1).print_list()
