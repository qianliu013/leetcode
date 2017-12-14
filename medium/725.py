# coding=utf-8

"""Split Linked List in Parts."""


def _solve(root, k):
    cur, length = root, 0
    while cur:
        cur = cur.next
        length += 1
    width, remainder = divmod(length, k)

    ans, cur = [], root
    for i in xrange(k):
        head = cur
        for _ in xrange(width + (i < remainder) - 1):
            cur = cur.next
        if cur:
            cur.next, cur = None, cur.next
        ans.append(head)
    return ans
