# coding=utf-8

""" Delete Operation for Two Strings.

>>> solve = _solve
>>> solve('sea', 'eat')
2
"""

# LCS(Longest Common Subsequence)

import bisect
import collections


def _solve(word1, word2):
    char_indexes = collections.defaultdict(list)
    for i, char in enumerate(word2):
        char_indexes[char].append(i)

    res = {len(word2): 0}
    for char in word1[::-1]:
        for last_index, total in res.items():
            bisect_index = bisect.bisect(char_indexes[char], last_index - 1)
            if 0 <= bisect_index - 1 < len(char_indexes[char]):
                new_last_index = char_indexes[char][bisect_index - 1]
                if new_last_index < last_index:
                    res[new_last_index] = max(res.get(new_last_index, 1), total + 1)
    return len(word1) + len(word2) - 2 * max(res.values() + [0])


def _solve1(word1, word2):
    len1, len2 = len(word1), len(word2)
    dp = [[0] * (len2 + 1) for _ in xrange(len1 + 1)]
    for i in xrange(len1):
        for j in xrange(len2):
            dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j], dp[i][j] + (word1[i] == word2[j]))
    return len1 + len2 - 2 * dp[len1][len2]


def _solve2(word1, word2):
    len1, len2 = len(word1), len(word2)
    dp = [0] * (len2 + 1)
    for char1 in word1:
        tmp = [0] * (len2 + 1)
        for i, char2 in enumerate(word2):
            tmp[i + 1] = max(dp[i + 1], tmp[i], dp[i] + (char1 == char2))
        dp = tmp
    return len1 + len2 - 2 * dp[-1]
