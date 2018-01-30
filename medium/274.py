# coding=utf-8
"""H-Index.

>>> solve = _solve
>>> solve([])
0
>>> solve([3, 3, 3])
3
>>> solve([3, 0, 6, 1, 5])
3
"""


def _solve(citations):
    if not citations:
        return 0
    length, counter = len(citations), [0] * (len(citations) + 1)
    for citation in citations:
        counter[length if citation > length else citation] += 1
    count = 0
    for i in xrange(length, 0, -1):
        count += counter[i]
        if count >= i:
            return i
    return 0


def _solve1(citations):
    if not citations:
        return 0
    citations.sort()
    for i, citation in enumerate(citations):
        if citation >= len(citations) - i:
            return len(citations) - i
    return 0
