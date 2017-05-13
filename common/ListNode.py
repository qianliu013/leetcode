# coding=utf-8

"""ListNode."""

from __future__ import print_function


class ListNode(object):
    """Definition for a list node."""

    def __init__(self, x):
        """Init node."""
        self.val = x
        self.next = None

    def __str__(self):
        """Print ListNode."""
        return str(self.val)

    @classmethod
    def from_list(cls, arr):
        """Init a node list from the input list."""
        if len(arr):
            head = cls(arr[0])
            cur = head
            for val in arr[1:]:
                cur.next = cls(val)
                cur = cur.next
            return head
        else:
            return None

    def print_list(self):
        """Print list."""
        cur = self.next
        print (self.val, end='')
        while cur:
            print (' -> ' + str(cur.val), end='')
            cur = cur.next
        print ()
