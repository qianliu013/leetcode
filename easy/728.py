# coding=utf-8

"""Self Dividing Numbers."""


def _solve(left, right):
    def _ok(num):
        for digit in str(num):
            if digit == '0':
                return False
            if num % int(digit) != 0:
                return False
        return True
    return [x for x in xrange(left, right + 1) if _ok(x)]
