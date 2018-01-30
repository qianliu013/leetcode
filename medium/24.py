# coding=utf-8

"""Swap Nodes in Pairs.

>>> solve = _solve
"""


def _solve(head):
    if not head or not head.next:
        return head
    head, prev, first = head.next, None, head
    while first and first.next:
        second = first.next
        first.next, second.next = second.next, first
        if prev:
            prev.next = second
        first, prev = first.next, first
    return head


# 虽然我认为递归并不是 constant space，但依旧写下解法
def _solve1(head):
    def _swap(head):
        if head and head.next:
            nxt = head.next
            head.next = _swap(head.next.next)
            nxt.next = head
            return nxt
        return head
    return _swap(head)
