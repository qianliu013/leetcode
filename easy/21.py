# coding=utf-8

"""Merge Two Sorted Lists."""

from __future__ import print_function
from ListNode import ListNode


def _solve(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

    dummy = ListNode(1)
    cur = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dummy.next


def _solve1(l1, l2):
    def _help(l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = _help(l1.next, l2)
            return l1
        else:
            l2.next = _help(l1, l2.next)
            return l2

    return _help(l1, l2)


if __name__ == '__main__':
    l1 = ListNode.from_list([1, 3])
    l2 = ListNode.from_list([0, 4])
    _solve(l2, l1).print_list()
