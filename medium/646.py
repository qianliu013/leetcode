# coding=utf-8

"""Maximum Length of Pair Chain.

>>> solve = _solve
>>> solve([[1, 2], [2, 3], [3, 4]])
2
"""


def _solve(pairs):
    ans, last_right = 0, float('-inf')
    for left, right in sorted(pairs, key=lambda pair: pair[1]):
        if left > last_right:
            ans += 1
            last_right = right
    return ans
