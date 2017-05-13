# coding=utf-8

"""Implement strStr()."""

from __future__ import print_function


def _solve(haystack, needle):
    if needle == '':
        return 0

    def _kmp(string):
        kmp_next = [0 for _ in string]
        j = 0
        for i in xrange(1, len(string)):
            while j > 0 and string[i] != string[j]:
                j = kmp_next[j - 1]
            if string[i] == string[j]:
                j += 1
            kmp_next[i] = j
        return kmp_next

    kmp_next = _kmp(needle)
    j = 0
    for i in xrange(len(haystack)):
        while j > 0 and haystack[i] != needle[j]:
            j = kmp_next[j - 1]
        if haystack[i] == needle[j]:
            j += 1
            if j == len(needle):
                return i - j + 1
    return -1


if __name__ == '__main__':
    print (_solve('ababababbabababac', 'ababac'))
    print (_solve('1121231', '12312'))
    print (_solve('123123', '31'))
    print (_solve('a', ''))
    print (_solve('', 'a'))
    print (_solve('', ''))
