# coding=utf-8

"""Daily Temperatures.

>>> solve = _solve
>>> solve([73, 74, 75, 71, 69, 72, 76, 73])
[1, 1, 4, 2, 1, 1, 0, 0]
"""


def _solve(temperatures):
    res, stack = [0] * len(temperatures), []
    for i, temperature in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temperature:
            res[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    return res
