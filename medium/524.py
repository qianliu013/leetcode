# coding=utf-8

"""Longest Word in Dictionary through Deleting.

>>> solve = _solve3
>>> solve('abpcplea', ["ale", "apple", "monkey", "plea"])
'apple'
>>> solve('abpcplea', ["a", "b", "c"])
'a'
"""

import bisect
import collections


def _solve(s, d):
    res, ans = collections.defaultdict(list), ''
    for i, char in enumerate(s):
        res[char].append(i)
    for string in d:
        start, found = -1, True
        for char in string:
            index = bisect.bisect_left(res[char], start + 1)
            if 0 <= index < len(res[char]):
                start = res[char][index]
            else:
                found = False
                break
        if found:
            if len(string) > len(ans) or (len(string) == len(ans) and ans > string):
                ans = string
    return ans


# 参考自 https://discuss.leetcode.com/topic/80887/short-python-solutions
def _solve1(s, d):
    for x in sorted(d, key=lambda x: (-len(x), x)):
        it = iter(s)
        if all(c in it for c in x):
            return x
    return ''


def _solve2(s, d):
    for string in sorted(d, key=lambda x: (-len(x), x)):
        i = -1
        for char in string:
            i = s.find(char, i + 1)
            if i == -1:
                break
        if i != -1:
            return string
    return ''


# 以上几种都是遍历 dictionary 中的字符串，也可以遍历原始字符串
# 参考自 https://discuss.leetcode.com/topic/94985/python-o-mn-time-o-n-space-pointer-based-solution-122ms-beats-98
def _solve3(s, d):
    candidates = collections.defaultdict(list)
    for word in d:
        candidates[word[0]].append((word, 0))

    res = (0, "")
    for char in s:
        words = candidates[char]
        candidates[char] = []
        for word, idx in words:
            if idx + 1 >= len(word):
                res = min(res, (-len(word), word))
            else:
                next_c = word[idx + 1]
                candidates[next_c].append((word, idx + 1))
    return res[1]
