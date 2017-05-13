# coding=utf-8

"""Palindrome Linked List."""

from ListNode import ListNode


def _solve(head):
    if not head:
        return True
    length = 0
    cur = head
    while cur:
        cur = cur.next
        length += 1
    prev, next = None, None
    cur = head
    for _ in xrange(0, length / 2):
        next = cur.next
        cur.next = prev
        prev, cur = cur, next
    if length & 1 == 1:
        cur = cur.next
    while cur:
        if cur.val != prev.val:
            return False
        cur = cur.next
        prev = prev.next
    return True


if __name__ == '__main__':
    print _solve(None)
    print _solve(ListNode(1))
    print _solve(ListNode.from_list([1, 2, 1]))
    print _solve(ListNode.from_list([1, 2, 2]))
    print _solve(ListNode.from_list([1, 2, 2, 1]))
    print _solve(ListNode.from_list([1, 2, 2, 2]))
