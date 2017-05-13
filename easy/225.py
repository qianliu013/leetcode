# coding=utf-8

"""Implement Stack using Queues."""

import collections


# One queue, push O(n)
class MyStack(object):
    """Implement Stack using Queues."""

    def __init__(self):
        """Initialize your data structure here."""
        self.queue = collections.deque()

    def push(self, x):
        """
        Push element x onto stack.

        :type x: int
        :rtype: void
        """
        length = len(self.queue)
        self.queue.append(x)
        for _ in range(length):
            self.queue.append(self.queue.popleft())

    def pop(self):
        """
        Remove the element on top of the stack and returns that element.

        :rtype: int
        """
        if self.empty():
            return None
        else:
            return self.queue.popleft()

    def top(self):
        """
        Get the top element.

        :rtype: int
        """
        if self.empty():
            return None
        else:
            return self.queue[0]

    def empty(self):
        """
        Return whether the stack is empty.

        :rtype: bool
        """
        return not self.queue


# One queue, pop O(n)
class MyStack1(object):
    """Implement Stack using Queues."""

    def __init__(self):
        """Initialize your data structure here."""
        self.queue = collections.deque()
        self._top = None

    def push(self, x):
        """
        Push element x onto stack.

        :type x: int
        :rtype: void
        """
        self._top = x
        self.queue.append(x)

    def pop(self):
        """
        Remove the element on top of the stack and returns that element.

        :rtype: int
        """
        for _ in range(len(self.queue) - 1):
            self._top = self.queue.popleft()
            self.queue.append(self._top)
        return self.queue.popleft()

    def top(self):
        """
        Get the top element.

        :rtype: int
        """
        return self._top

    def empty(self):
        """
        Return whether the stack is empty.

        :rtype: bool
        """
        return not self.queue


# Two queues, pop O(n)
class MyStack2(object):
    """Implement Stack using Queues."""

    def __init__(self):
        """Initialize your data structure here."""
        self.queue, self.auxiliary_queue = collections.deque(), collections.deque()
        self._top = None

    def push(self, x):
        """
        Push element x onto stack.

        :type x: int
        :rtype: void
        """
        self._top = x
        self.queue.append(x)

    def pop(self):
        """
        Remove the element on top of the stack and returns that element.

        :rtype: int
        """
        length = len(self.queue)
        for _ in range(length - 1):
            self._top = self.queue.popleft()
            self.auxiliary_queue.append(self._top)
        self.queue, self.auxiliary_queue = self.auxiliary_queue, self.queue
        return self.auxiliary_queue.popleft()

    def top(self):
        """
        Get the top element.

        :rtype: int
        """
        return self._top

    def empty(self):
        """
        Return whether the stack is empty.

        :rtype: bool
        """
        return not self.queue


def _test_stack(stack):
    print 'pop: {0}, then top: {1} -- empty: {2}'.format(stack.pop(), stack.top(), stack.empty())


if __name__ == '__main__':
    MY_STACK = MyStack1()
    MY_STACK.push(1)
    MY_STACK.push(2)
    MY_STACK.push(3)
    MY_STACK.push(4)
    MY_STACK.push(5)
    _test_stack(MY_STACK)
    _test_stack(MY_STACK)
    _test_stack(MY_STACK)
    _test_stack(MY_STACK)
    _test_stack(MY_STACK)
