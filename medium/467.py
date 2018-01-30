# coding=utf-8
"""Unique Substrings in Wraparound String.

>>> solve = _solve
>>> solve('cac')
2
>>> solve('zab')
6
>>> solve('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz')
1027
"""


# 考虑以 a-z 每个字母开头的字符串
def _solve(p):
    if not p:
        return 0
    dp = {chr(97 + i): 0 for i in xrange(26)}
    nxt = {chr(97 + i): chr(97 + i + 1) for i in xrange(25)}
    nxt['z'] = 'a'
    p += '#'
    start, count, length = 0, 1, len(p)
    for i in xrange(1, length):
        if nxt[p[i - 1]] == p[i]:
            count += 1
        else:
            for ch in p[start:i]:
                if count > dp[ch]:
                    dp[ch] = count
                else:
                    break
                count -= 1
            start = i
            count = 1
    return sum(dp.values())


# 如果考虑以某个字母结束，代码会简洁很多
def _solve1(p):
    if not p:
        return 0
    dp = {chr(97 + i): 0 for i in xrange(26)}
    nxt = {chr(97 + i): chr(97 + i + 1) for i in xrange(25)}
    nxt['z'] = 'a'
    count, length = 1, len(p)
    dp[p[0]] = 1
    for i in xrange(1, length):
        if nxt[p[i - 1]] == p[i]:
            count += 1
        else:
            count = 1
        if count > dp[p[i]]:
            dp[p[i]] = count
    return sum(dp.values())
