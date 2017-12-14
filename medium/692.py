# coding=utf-8

"""Top K Frequent Words.

>>> solve = _solve2
>>> _solve(["i", "love", "leetcode", "i", "love", "coding"], 2)
['i', 'love']
>>> _solve(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4)
['the', 'is', 'sunny', 'day']
"""

import collections
import functools
import heapq


# O(n*logN)
def _solve(words, k):
    counter = collections.Counter(words)
    res = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return [word for word, _ in res[:k]]


# heap, O(N + k*logN)
def _solve1(words, k):
    counter = collections.Counter(words)
    heap = [(-freq, word) for word, freq in counter.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in xrange(k)]


# python 要实现 O(N * logK) 稍微复杂些
# 代码参考自 https://discuss.leetcode.com/topic/107256/python-3-solution-with-o-nlogk-and-o-n
def _solve2(words, k):
    @functools.total_ordering
    class Element(object):
        def __init__(self, count, word):
            self.count, self.word = count, word

        def __lt__(self, other):
            return self.word > other.word if self.count == other.count else self.count < other.count

        def __eq__(self, other):
            return self.count == other.count and self.word == other.word

    counter = collections.Counter(words)
    heap = []
    heapq.heapify(heap)
    for word, freq in counter.items():
        heapq.heappush(heap, Element(freq, word))
        if len(heap) > k:
            heapq.heappop(heap)
    return [heapq.heappop(heap).word for _ in xrange(k)][::-1]
