# coding=utf-8
"""Partition List.

>>> solve = _solve
>>> solve(ListNode.from_list([]), 0)
>>> solve(ListNode.from_list([1, 4, 3, 2, 5, 2]), 0).to_list()
[1, 4, 3, 2, 5, 2]
>>> solve(ListNode.from_list([1, 4, 3, 2, 5, 2]), 3).to_list()
[1, 2, 2, 4, 3, 5]
"""

from ListNode import ListNode


def _solve(head, x):
    faker1, faker2 = ListNode(float('-inf')), ListNode(x)
    head1, head2 = faker1, faker2
    while head:
        if head.val < x:
            head1.next = head
            head1 = head1.next
        else:
            head2.next = head
            head2 = head2.next
        head = head.next
    head1.next, head2.next = faker2.next, None
    return faker1.next
