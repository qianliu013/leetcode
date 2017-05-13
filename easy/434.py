# coding=utf-8

"""Number of Segments in a String."""


def _solve(s):
    return len(s.split())


if __name__ == '__main__':
    print _solve('123 123')
