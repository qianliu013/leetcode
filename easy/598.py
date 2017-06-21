# coding=utf-8

"""Range Addition II."""

from __future__ import print_function


def _solve(m, n, ops):
    return min([op[0] for op in ops]) * min([op[1] for op in ops]) if ops else m * n


if __name__ == '__main__':
    print (_solve(3, 3, []))
    print (_solve(3, 3, [[2, 2], [3, 3]]))
