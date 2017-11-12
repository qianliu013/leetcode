# coding=utf-8

"""Odd Even Linked List.

>>> solve = _solve
>>> solve()

"""

from ListNode import ListNode


def _solve(head):
    if not head or not head.next:
        return head
    odd, even, prev_odd, head_odd = head, head.next, head, head.next
    while True:
        if even:
            odd.next = even.next
            prev_odd, odd = odd, odd.next
        else:
            odd.next = head_odd
            break
        if odd:
            even.next = odd.next
            even = even.next
        else:
            prev_odd.next, even.next = head_odd, None
            break
    return head


def _solve1(head):
    if head:
        odd, even, head_even = head, head.next, head.next
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        odd.next = head_even
    return head


def _generate_nodes(num):
    head = ListNode(0)
    cur = head
    for i in xrange(num):
        cur.next = ListNode(i + 1)
        cur = cur.next
    return head.next if head.next else head


_solve1(_generate_nodes(0)).print_list()
_solve1(_generate_nodes(1)).print_list()
_solve1(_generate_nodes(2)).print_list()
_solve1(_generate_nodes(3)).print_list()
_solve1(_generate_nodes(4)).print_list()
