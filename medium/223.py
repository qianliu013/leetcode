# coding=utf-8
"""Rectangle Area.

>>> solve = _solve
>>> solve(-2, -2, 2, 2, -2, -2, 2, 2)
16
>>> solve(0, 0, 0, 0, -1, -1, 1, 1)
4
"""


def _solve(A, B, C, D, E, F, G, H):
    overlap = max(min(C, G) - max(A, E), 0) * max(min(D, H) - max(B, F), 0)
    return (A - C) * (B - D) + (E - G) * (F - H) - overlap
