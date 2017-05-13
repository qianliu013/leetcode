# coding=utf-8

"""Linked List Cycle."""

from ListNode import ListNode


def _solve(head):
    if not head or not head.next:
        return False
    quick, slow = head.next, head
    while quick and quick is not slow:
        slow = slow.next
        quick = quick.next and quick.next.next
    return quick == slow


# 翻转列表，如果有环，翻转列表后，一定会回到头部
# 这种方法会破坏原 NodeList

def _solve1(head):
    prev, cur, next = None, head, None
    while cur and cur.next:
        if cur.next == head:
            return True
        next = cur.next
        cur.next = prev
        prev, cur = cur, next
    return False


if __name__ == '__main__':
    RECYCLE_NODE = ListNode.from_list([1, 2, 3])
    RECYCLE_NODE.next.next.next = RECYCLE_NODE
    node1 = ListNode(1)
    node1.next = node1
    print _solve1(RECYCLE_NODE)
    print _solve(node1)
    print _solve1(ListNode.from_list([1, 2, 3]))
    print _solve1(ListNode(1))
    print _solve1(None)
