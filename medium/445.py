# coding=utf-8

"""Add Two Numbers II."""

from ListNode import ListNode


def _solve(l1, l2):
    s1, s2 = [], []
    while l1:
        s1.append(str(l1.val))
        l1 = l1.next
    while l2:
        s2.append(str(l2.val))
        l2 = l2.next
    dummy = ListNode(0)
    cur = dummy
    for ch in str(int(''.join(s1)) + int(''.join(s2))):
        node = ListNode(int(ch))
        cur.next, cur = node, node
    return dummy.next
