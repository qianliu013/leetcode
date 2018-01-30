# coding=utf-8
"""Sort List.

>>> solve = _solve
>>> solve(ListNode.from_list([1, 2, 3])).to_list() == solve(ListNode.from_list([3, 1, 2])).to_list() == solve(ListNode.from_list([3, 2, 1])).to_list()
True
"""

from ListNode import ListNode


def _solve(head):
    if not head:
        return head
    faker = ListNode(float('-inf'))

    def _sort(head):
        if not head or not head.next:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head1, head2 = head, slow.next
        slow.next = None
        head1 = _sort(head1)
        head2 = _sort(head2)

        prev = faker
        while head1 and head2:
            if head1.val < head2.val:
                prev.next = head1
                head1 = head1.next
            else:
                prev.next = head2
                head2 = head2.next
            prev = prev.next
        prev.next = head1 or head2
        return faker.next

    return _sort(head)


# 题中要求使用 constant space，递归空间复杂度为 O(log(n))，因而需要改为 bottom-up 的迭代版本
# 代码参考自：https://discuss.leetcode.com/topic/10382/bottom-to-up-not-recurring-with-o-1-space-complextity-and-o-nlgn-time-complextity
def _solve1(head):
    if not head:
        return head
    faker = ListNode(float('-inf'))
    faker.next = head

    def _split(head, cnt):
        while cnt > 1 and head:
            head = head.next
            cnt -= 1
        if head:
            head.next, nxt = None, head.next
            return nxt
        return None

    def _merge(head1, head2, head):
        while head1 and head2:
            if head1.val < head2.val:
                head.next = head1
                head1 = head1.next
            else:
                head.next = head2
                head2 = head2.next
            head = head.next
        head.next = head1 or head2
        while head.next:
            head = head.next
        return head

    cur, length = head, 0
    while cur:
        length += 1
        cur = cur.next
    step = 1
    while step < length:
        last_tail, new_start = faker, faker.next
        while new_start:
            left = new_start
            right = _split(left, step)
            new_start = _split(right, step)
            last_tail = _merge(left, right, last_tail)
        step <<= 1
    return faker.next
