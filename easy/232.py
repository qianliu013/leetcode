# coding=utf-8

"""Implement Queue using Stacks."""


# 一个 stack 的方法就是递归，使 push 或者 pop/peek 方法复杂化
# 其实相当于还是两个 stack
class MyQueue(object):
    """Implement Queue using Stacks."""

    def __init__(self):
        """Initialize your data structure here."""
        self.in_stack, self.out_stack = [], []

    def push(self, x):
        """
        Push element x to the back of queue.

        :type x: int
        :rtype: void
        """
        self.in_stack.append(x)

    def pop(self):
        """
        Remove the element from in front of queue and returns that element.

        :rtype: int
        """
        self.__help()
        return self.out_stack.pop() if self.out_stack else None

    def peek(self):
        """
        Get the front element.

        :rtype: int
        """
        self.__help()
        return self.out_stack[-1] if self.out_stack else None

    def empty(self):
        """
        Return whether the queue is empty.

        :rtype: bool
        """
        return not self.in_stack and not self.out_stack

    def __help(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


def _print(queue):
    print 'peek: {0}, empty: {1}'.format(queue.peek(), queue.empty())


if __name__ == '__main__':
    QUEUE = MyQueue()
    QUEUE.push(1)
    _print(QUEUE)
    QUEUE.push(2)
    _print(QUEUE)
    print QUEUE.pop()
    _print(QUEUE)
    QUEUE.push(3)
    _print(QUEUE)
    print QUEUE.pop()
    _print(QUEUE)
    print QUEUE.pop()
    _print(QUEUE)
