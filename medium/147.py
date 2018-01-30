# coding=utf-8
"""Insertion Sort List.

>>> solve = _solve
"""

from ListNode import ListNode
import test_tools


# 此题直接裸的插入排序的 python 很容易超时，需要优化
@test_tools.log_execution_time('Insert sort')
def _solve(head):
    if not head:
        return head
    little = faker = ListNode(float('-inf'))
    faker.next = head
    prev, cur = head, head.next
    while cur:
        if prev.val <= cur.val:
            prev, cur = cur, cur.next
            continue
        # 下面这个 if 是最重要的优化
        if little.val > cur.val:
            little = faker
        while little.next.val < cur.val:
            little = little.next
        prev.next = cur.next
        little.next, cur.next = cur, little.next
        cur = prev.next
    return faker.next


# 在得到 TLE 后，我有点怀疑是时间复杂度的问题，因此写了下面的归并排序代码
@test_tools.log_execution_time('Merge sort')
def _solve1(head):
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
        if head1:
            prev.next = head1
        else:
            prev.next = head2
        return faker.next

    return _sort(head)


if __name__ == '__main__':
    _solve(ListNode.from_list(range(1, 5001)))
    _solve1(ListNode.from_list(range(1, 5001)))
