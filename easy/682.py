# coding=utf-8

"""Baseball Game.

>>> solve = _solve
>>> solve(["5", "2", "C", "D", "+"])
30
>>> solve(["5", "-2", "4", "C", "D", "9", "+", "+"])
27
"""


def _solve(ops):
    stack = [0, 0]
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'C':
            stack.pop()
        elif op == 'D':
            stack.append(stack[-1] * 2)
        else:
            stack.append(int(op))
    return sum(stack)
