# coding=utf-8

"""Sort Characters By Frequency.

>>> solve = _solve
>>> solve('tree')
'eert'
>>> _solve('cccaaa')
'aaaccc'
>>> _solve('Aabb')
'bbAa'
"""

import collections
import operator


def _solve(s):
    result = {}
    for ch in s:
        result[ch] = result.get(ch, 0) + 1
    # return ''.join([ch * frequency for ch, frequency in
    #                 sorted(result.items(), key=operator.itemgetter(1), reverse=True)])
    # 或者直接排序字符串，但会慢很多
    # return ''.join(sorted(s, key=lambda ch: (result[ch], -ord(ch)), reverse=True))


def _solve1(s):
    return "".join([char * times for char, times in collections.Counter(s).most_common()])


def _solve2(s):
    frequency, bucket = {}, [''] * (len(s) + 1)
    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1
    for ch, times in frequency.items():
        bucket[times] += ch * times
    return ''.join(bucket[i] for i in xrange(len(s), 0, -1) if bucket[i])
