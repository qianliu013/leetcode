# coding=utf-8

"""Group Anagrams.

>>> solve = _solve
>>> sorted(solve(["eat", "tea", "tan", "ate", "nat", "bat"]))
[['bat'], ['eat', 'tea', 'ate'], ['tan', 'nat']]
"""

import collections


def _solve(strs):
    res = collections.defaultdict(list)
    for word in strs:
        res[''.join(sorted(word))].append(word)
    return res.values()
