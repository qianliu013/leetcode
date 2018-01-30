# coding=utf-8
"""Remove Nth Node From End of List

>>> solve = _solve
"""

from ListNode import ListNode


def _solve(head, n):
    dumpy = ListNode(0)
    dumpy.next = head
    head1 = head2 = dumpy
    for _ in xrange(n):
        head2 = head2.next
    while head2.next:
        head1 = head1.next
        head2 = head2.next
    head1.next = head1.next.next
    return dumpy.next
