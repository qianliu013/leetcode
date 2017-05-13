# coding=utf-8

"""Remove Linked List Elements."""

from ListNode import ListNode


def _solve(head, val):
    dump = ListNode('a')
    dump.next = head
    prev, cur = dump, head
    while cur:
        if cur.val == val:
            prev.next = cur.next
            cur = cur.next
        else:
            prev, cur = cur, cur.next

    return dump.next


if __name__ == '__main__':
    print _solve(None, 0)
    _solve(ListNode(1), 0).print_list()
    print _solve(ListNode(1), 1)
    print _solve(ListNode.from_list([1, 1, 1, 1]), 1)
    _solve(ListNode.from_list([1, 2, 6, 4, 5, 6, 6]), 6).print_list()
