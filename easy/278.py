# coding=utf-8

"""First Bad Version."""

from __future__ import print_function


def isBadVersion(version):
    """API."""
    bad_version = 3
    if version < bad_version:
        return False
    return True


def _solve(n):
    start, end = 1, n
    while start <= end:
        mid = start + (end - start) / 2
        if isBadVersion(mid):
            end = mid - 1
        else:
            start = mid + 1
    return start


if __name__ == '__main__':
    for i in xrange(10):
        print (i, '->', _solve(i))
