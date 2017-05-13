# coding=utf-8

"""Intersection of Two Linked Lists."""

from ListNode import ListNode


def _solve(headA, headB):
    num_a = num_b = 0
    cur_a, cur_b = headA, headB
    while cur_a:
        cur_a = cur_a.next
        num_a += 1
    while cur_b:
        cur_b = cur_b.next
        num_b += 1
    if cur_a != cur_b:
        return None
    diff = num_a - num_b
    while diff != 0:
        if diff > 0:
            headA = headA.next
            diff -= 1
        else:
            headB = headB.next
            diff += 1
    while headA and headB and headA != headB:
        headA, headB = headA.next, headB.next
    return headA


def _solve1(headA, headB):
    if not headA or not headB:
        return None
    cur_a, cur_b = headA, headB
    while cur_a != cur_b:
        cur_a = cur_a.next if cur_a else headB
        cur_b = cur_b.next if cur_b else headA
    return cur_a

# 此外，还有一种方法
# https://discuss.leetcode.com/topic/26018/python-solution-o-n-time-and-o-1-space
# 这种方法相比上两种稍微难理解点，因为最后的结果的正确性需要证明下，代码也更多一些，而且也没有运行优势
# 因此不再列出


if __name__ == '__main__':
    print _solve1(None, None)
    print _solve1(ListNode(1), None)
    print _solve1(None, ListNode(1))
    print _solve1(ListNode(1), ListNode(1))
    HEAD1 = ListNode.from_list([4, 5, 6, 7, 8, 0, 1])
    HEAD2 = ListNode.from_list([1, 2, 3])
    HEAD2.next = HEAD1.next.next.next
    HEAD1.print_list()
    HEAD2.print_list()
    print _solve1(HEAD1, HEAD2)
    print _solve1(HEAD2, HEAD1)
    HEAD2 = ListNode.from_list([1, 2, 3])
    HEAD2.next.next = HEAD1.next.next
    HEAD1.print_list()
    HEAD2.print_list()
    print _solve1(HEAD1, HEAD2)
    print _solve1(HEAD2, HEAD1)
