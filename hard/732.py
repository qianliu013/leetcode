# coding=utf-8

"""My Calendar III.

>>> solve = _solve
>>> solve()

"""

import bisect


# 由于 python 没有 TreeMap，因此只能通过 list + bisect 来达到有序的 collection
# Treemap 的解法可以参考 https://discuss.leetcode.com/category/1616
class MyCalendarThree(object):

    def __init__(self):
        self.__max = 0
        self.__nodes = [[-1, 0], [1e9 + 1, 0]]

    def book(self, start, end):
        start_i = bisect.bisect(self.__nodes, [start])
        if self.__nodes[start_i][0] != start:
            self.__nodes.insert(start_i, [start, self.__nodes[start_i - 1][1]])
        end_i = bisect.bisect(self.__nodes, [end])
        if self.__nodes[end_i][0] != end:
            self.__nodes.insert(end_i, [end, self.__nodes[end_i - 1][1]])
        for i in xrange(start_i, end_i):
            self.__nodes[i][1] += 1
            self.__max = max(self.__max, self.__nodes[i][1])
        return self.__max
