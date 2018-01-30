# coding=utf-8

"""Shortest Completing Word.

>>> solve = _solve
>>> solve("1s3 PSt", ["step", "steps", "stripe", "steeple"])
'steps'
>>> solve("1s3 456", ["looks", "pest", "stew", "show"])
'pest'
"""

import collections


def _solve(licensePlate, words):
    def _counter_alpha(string):
        string = string.lower()
        res = collections.defaultdict(int)
        for ch in string:
            if ch.isalpha():
                res[ch] += 1
        return res

    license_dict, ans = _counter_alpha(licensePlate), '-' * 1001
    for word in words:
        tmp = _counter_alpha(word)
        if len(word) < len(ans) and all([(ch in tmp and tmp[ch] >= value) for ch, value in license_dict.items()]):
            ans = word
    return ans
