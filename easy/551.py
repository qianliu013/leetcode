# coding=utf-8

"""Student Attendance Record I."""

from __future__ import print_function


def _solve(s):
    absent = 0
    for index in xrange(len(s)):
        if s[index] == 'A':
            absent += 1
            if absent > 1:
                return False
        if s[index] == 'L':
            if index > 1 and s[index - 1] == 'L' and s[index - 2] == 'L':
                return False
    return True


if __name__ == '__main__':
    print (_solve('PPALLP'))
    print (_solve('PPALLL'))
    print (_solve('LLL'))
