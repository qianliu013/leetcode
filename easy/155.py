# coding=utf-8

"""Min Stack."""

from __future__ import print_function

import collections


class MinStack(object):
    """Min Stack."""

    def __init__(self):
        """Initialize your data structure here."""
        self.__min_deque = collections.deque()
        self.__data_deque = collections.deque()

    def push(self, x):
        """
        Push x.

        :type x: int
        :rtype: void
        """
        self.__data_deque.append(x)
        self.__min_deque.append(min(x, self.__min_deque[-1] if self.__min_deque else x))

    def pop(self):
        """
        Pop.

        :rtype: void
        """
        self.__data_deque.pop()
        self.__min_deque.pop()

    def top(self):
        """
        Top.

        :rtype: int
        """
        return self.__data_deque[-1]

    def getMin(self):
        """
        GetMin.

        :rtype: int
        """
        return self.__min_deque[-1]


# 参考自 https://discuss.leetcode.com/topic/4953/share-my-java-solution-with-only-one-stack
# 一个栈实现 min stack，不同于很多代码在一个 stack 加入 pair 或者是把 min 压入栈
# 这种方法是真正意义的一个栈实现 stack
class MinStack1(object):
    """Min Stack."""

    def __init__(self):
        """Initialize your data structure here."""
        self.__stack = []
        self.__min = 0

    def push(self, x):
        """
        Push x.

        :type x: int
        :rtype: void
        """
        if self.__stack:
            self.__stack.append(x - self.__min)
            if x < self.__min:
                self.__min = x
        else:
            self.__stack.append(0)
            self.__min = x

    def pop(self):
        """
        Pop.

        :rtype: void
        """
        top = self.__stack.pop()
        if top < 0:
            self.__min = self.__min - top

    def top(self):
        """
        Top.

        :rtype: int
        """
        top = self.__stack[-1]
        if top > 0:
            return self.__stack[-1] + self.__min
        else:
            return self.__min

    def getMin(self):
        """
        GetMin.

        :rtype: int
        """
        return self.__min


if __name__ == '__main__':
    MIN_STACK = MinStack1()
    MIN_STACK.push(3)
    MIN_STACK.push(2)
    MIN_STACK.push(1)
    print (MIN_STACK.top())
    print (MIN_STACK.getMin())
    MIN_STACK.pop()
    print (MIN_STACK.top())
    print (MIN_STACK.getMin())
    MIN_STACK.pop()
    print (MIN_STACK.top())
    print (MIN_STACK.getMin())
