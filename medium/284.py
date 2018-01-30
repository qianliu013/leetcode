# coding=utf-8
"""Peeking Iterator."""


class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.__nums = nums
        self.__i = -1

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.__i < len(self.__nums) - 1

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.__i += 1
        return self.__nums[self.__i]


# 下面代码可以去掉 advanced 值，可以通过 val is None 来判断是否推进过
class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.__iterator = iterator
        self.__advanced = False
        self.__val = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if not self.__advanced:
            self.__val = self.__iterator.next()
            self.__advanced = True
        return self.__val

    def next(self):
        """
        :rtype: int
        """
        if not self.__advanced:
            return self.__iterator.next()
        self.__advanced = False
        return self.__val

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.__advanced or self.__iterator.hasNext()


# 只在一个地方调用 next 会更好
class PeekingIterator1(object):
    def __init__(self, iterator):
        self.__iterator = iterator
        self.__cache = self.__iterator.next() if self.__iterator.hasNext() else None

    def peek(self):
        return self.__cache

    def next(self):
        ret = self.__cache
        self.__cache = self.__iterator.next() if self.__iterator.hasNext() else None
        return ret

    def hasNext(self):
        return self.__cache is not None


def _test():
    iterator = PeekingIterator1(Iterator([3, 2, 1]))
    assert iterator.peek() == 3
    assert iterator.next() == 3
    assert iterator.next() == 2
    assert iterator.peek() == 1
    assert iterator.hasNext()
    assert iterator.next() == 1
    assert not iterator.hasNext()


_test()
