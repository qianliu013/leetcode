# coding=utf-8

"""Longest Common Prefix."""

import os


# Horizontal scanning
def _solve(strs):
    if not strs:
        return ''
    ans, cur = strs[0], len(strs[0])
    for str in strs[1:]:
        cur = min(len(str), cur)
        ans = ans[0:cur]
        for i in xrange(cur):
            if str[i] != ans[i] and cur > i:
                cur, ans = i, str[0:i]
                break
    return ans


# Vertical scanning
def _solve1(strs):
    if not strs:
        return ''
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i == len(strs[j]) or strs[0][i] != strs[j][i]:
                return strs[0][0:i]
    return strs[0]


# sort
def _solve2(strs):
    if not strs:
        return ''
    strings = sorted(strs)
    first, last = strings[0], strings[-1]
    for i in range(len(first)):
        if len(last) > i and last[i] != first[i]:
            return first[0:i]
    return first


def _solve3(strs):
    return os.path.commonprefix(strs)


if __name__ == '__main__':
    print _solve3([])
    print _solve3(['12312'])
    print _solve3(['12312', '12312'])
    print _solve3(['12312', '12311', '1233'])
    print _solve3(['ccc', 'c'])
    print _solve3(["flower", "flow", "flight"])
