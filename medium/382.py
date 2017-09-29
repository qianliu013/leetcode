# coding=utf-8

"""Linked List Random Node."""

import random


# Reservoir Sampling，证明可参考 http://www.cnblogs.com/HappyAngel/archive/2011/02/07/1949762.html
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        val, cur = self.head.val, self.head.next
        count = 1
        while cur:
            if random.randint(0, count) < 1:
                val = cur.val
            cur, count = cur.next, count + 1
        return val


# 上述代码其实并不快，主要是因为反复的求解 rand
# 可以使用 ["buffered" reservoir sampling](https://discuss.leetcode.com/topic/53844/buffered-reservoir-sampling) 以加速
# 另一种做法是在 __init__ 缓存长度
class Solution1(object):

    def __init__(self, head):
        self.head = head
        count = 0
        while head:
            head = head.next
            count += 1
        self.length = count

    def getRandom(self):

        count, cur = random.randrange(self.length), self.head
        for _ in xrange(count):
            cur = cur.next
        return cur.val
