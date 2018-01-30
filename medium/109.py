# coding=utf-8
"""Convert Sorted List to Binary Search Tree.

>>> solve = _solve
"""

# 此题的思路是：对半分链表，分别构造；值得注意的是，下面解法的复杂度应该都是 O(n*log(n))，不是 O(n)

from TreeNode import TreeNode


# 中序遍历构造
def _solve(head):
    cur, count = [head], 0

    def _build(count):
        if count:
            mid = count / 2
            root = TreeNode(0)
            root.left = _build(mid)
            root.val = cur[0].val
            cur[0] = cur[0].next
            root.right = _build(count - mid - 1)
            return root
        return None

    while head:
        head = head.next
        count += 1
    return _build(count)


# 主动传入链表
def _solve1(head):
    def _build(head, tail):
        if head == tail:
            return None
        slow = fast = head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next
        root = TreeNode(slow.val)
        root.left, root.right = _build(head, slow), _build(slow.next, tail)
        return root

    if head:
        return _build(head, None)
    return None
