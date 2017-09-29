# coding=utf-8

"""Palindromic Substrings.

>>> solve = _solve3
>>> solve('aba')
4
>>> solve('abc')
3
>>> solve('abba')
6
>>> solve('aaaaa')
15
"""


def _solve(s):
    length, res = len(s), 0
    for i in xrange(0, length):
        for j in xrange(i + 1, length + 1):
            if s[i:j] == s[i:j][::-1]:
                res += 1
    return res


def _solve1(s):
    if not s:
        return 0

    ans, length = [0], len(s)

    def _extend(s, left, right):
        while left >= 0 and right < length and s[left] == s[right]:
            ans[0] += 1
            left -= 1
            right += 1

    for i in xrange(length):
        _extend(s, i, i)
        _extend(s, i, i + 1)

    return ans[0]


# dp
def _solve2(s):
    length = len(s)
    dp = [[False] * length for _ in xrange(length)]
    ans = 0
    for i in xrange(length):
        for j in xrange(i, -1, -1):
            dp[j][i] = (s[i] == s[j] and (i - j < 3 or dp[j + 1][i - 1]))
            if dp[j][i]:
                ans += 1
    return ans


# O(n), Implementing Manacher's algorithm
# 参考 https://discuss.leetcode.com/topic/96822/python-straightforward-with-explanation-bonus-o-n-solution
# 理解可参考 http://www.cnblogs.com/bitzhuwei/p/Longest-Palindromic-Substring-Part-II.html
def _solve3(s):
    def _manachers(s):
        new_s = '^#' + '#'.join(s) + '#$'
        radius = [0] * len(new_s)
        center = right = 0
        for i in xrange(1, len(new_s) - 1):
            if i < right:
                radius[i] = min(right - i, radius[2 * center - i])
            while new_s[i + radius[i] + 1] == new_s[i - radius[i] - 1]:
                radius[i] += 1
            if i + radius[i] > right:
                center, right = i, i + radius[i]
        return radius
    return sum((v + 1) / 2 for v in _manachers(s))
