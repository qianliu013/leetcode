# coding=utf-8

"""Find Smallest Letter Greater Than Target.

>>> solve = _solve
>>> [solve(['c', 'f', 'j'], char) for char in 'acdgjk']
['c', 'f', 'f', 'j', 'c', 'c']
"""


def _solve(letters, target):
    low, high = 0, len(letters)
    while low < high:
        mid = (low + high) / 2
        if target < letters[mid]:
            high = mid
        else:
            low = mid + 1
    # 上面代码其实就是 bisect.bisect_right
    return letters[low % len(letters)]
