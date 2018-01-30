# coding=utf-8
"""H-Index II.

>>> solve = _solve1
>>> solve([])
0
>>> solve([100])
1
>>> solve([1, 10, 100])
2
"""


def _solve(citations):
    if not citations:
        return 0
    low, high, length = 0, len(citations), len(citations)
    while low < high:
        mid = (low + high) / 2
        if length - mid > citations[mid]:
            low = mid + 1
        else:
            high = mid
    return length - low


# 如果判断不等式有等号，则需要变更返回值，因为最终值的意义不同
def _solve1(citations):
    if not citations:
        return 0
    low, high, length = 0, len(citations), len(citations)
    while low < high:
        mid = (low + high) / 2
        if length - mid >= citations[mid]:
            low = mid + 1
        else:
            high = mid
    return max(citations[low - 1] if low else 0, length - low)
