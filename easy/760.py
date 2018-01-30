# coding=utf-8
"""Find Anagram Mappings.

>>> solve = _solve
>>> solve([12,28,46,32,50], [50,12,32,46,28])
[1, 4, 3, 2, 0]
"""


def _solve(A, B):
    indexes = {num: i for i, num in enumerate(B)}
    return [indexes[num] for num in A]
