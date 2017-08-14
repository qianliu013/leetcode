# coding=utf-8

"""Set Mismatch.

>>> solve = _solve
>>> solve([1, 2, 2, 4])
[2, 3]
"""

import collections


def _solve(nums):
    counter = collections.Counter(nums)
    result = [num for num in xrange(1, len(nums) + 1) if counter[num] != 1]
    return result if counter[result[0]] == 2 else result[::-1]


