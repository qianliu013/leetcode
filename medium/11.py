# coding=utf-8

"""Container With Most Water.

>>> solve = _solve
>>> solve([1, 2, 3, 4, 5, 6])
9
"""


def _solve(height):
    left, right = 0, len(height) - 1
    ans = 0
    while left < right:
        ans = max(ans, (right - left) * min(height[left], height[right]))
        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return ans
