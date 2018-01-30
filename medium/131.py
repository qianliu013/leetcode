# coding=utf-8
"""Palindrome Partitioning.

>>> solve = _solve1
>>> len(solve('a' * 10)) == 1 << (10 - 1)
True
"""


def _solve(s):
    def _dfs(start):
        if start == len(s):
            return [[]]
        res = []
        for end in xrange(start + 1, len(s) + 1):
            cur = s[start:end]
            if cur == cur[::-1]:
                res.extend([[cur] + nxt for nxt in _dfs(end)])
        return res

    return _dfs(0)


# 使用 dp，顺便处理 s 的所有子串是否回文；注意整体复杂度并不是 O(n ^ 2)，是 O(2 ^ n)
# 代码参考自：https://discuss.leetcode.com/topic/2884/my-java-dp-only-solution-without-recursion-o-n-2
def _solve1(s):
    length, res = len(s), [[[]]]
    palindrome = set()
    for i in xrange(length):
        res.append([])
        for left in xrange(i + 1):
            if s[left] == s[i] and (i - left <= 1 or (left + 1, i - 1) in palindrome):
                palindrome.add((left, i))
                res[i + 1].extend([prev + [s[left:i + 1]] for prev in res[left]])
    return res[-1]
