# coding=utf-8

"""Add Two Numbers."""

from ListNode import ListNode


def _solve(l1, l2):
    dummy, carry = ListNode(None), 0
    cur = dummy
    while l1 or l2 or carry:
        if l1:
            carry, l1 = carry + l1.val, l1.next
        if l2:
            carry, l2 = carry + l2.val, l2.next
        carry, val = divmod(carry, 10)
        cur.next = cur = ListNode(val)
    return dummy.next
