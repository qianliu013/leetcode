# coding=utf-8

"""My Calendar I."""

import bisect


class MyCalendar(object):

    def __init__(self):
        self.__books = []

    def book(self, start, end):
        for s, e in self.__books:
            if s < end and start < e:
                # or max(s, start) < min(end, e)
                return False
        self.__books.append((start, end))
        return True


# 来自 solution：https://leetcode.com/articles/my-calendar-i/
# 由于 books 不可能相交，很容易构造一颗二叉树
class Node(object):
    __slots__ = 'start', 'end', 'left', 'right'

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False


class MyCalendar1(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))


class MyCalendar2(object):

    def __init__(self):
        self.__books = []

    def book(self, start, end):
        idx = bisect.bisect(self.__books, (start, ))
        if idx - 1 >= 0 and self.__books[idx - 1][1] > start:
            return False
        elif idx < len(self.__books) and self.__books[idx][0] < end:
            return False
        else:
            bisect.insort(self.__books, (start, end))
            return True
