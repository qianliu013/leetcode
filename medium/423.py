# coding=utf-8

"""Reconstruct Original Digits from English."""


import collections
import random


# 其实可以视为求解一个多元一次方程组，由于方程组比较简单，手动计算即可
def _solve(s):
    res = collections.Counter(s)
    totals = [0] * 10
    totals[0], totals[2], totals[4], totals[6], totals[8] = res['z'], res['w'], res['u'], res['x'], res['g']
    totals[1], totals[3], totals[5], totals[7] = (res['o'] - totals[0] - totals[2] - totals[4],
                                                  res['h'] - totals[8],
                                                  res['f'] - totals[4],
                                                  res['s'] - totals[6])
    totals[9] = res['i'] - totals[5] - totals[6] - totals[8]
    return ''.join([str(digit) * total for digit, total in enumerate(totals)])


for _ in xrange(20):
    in_s, out_s = '', ''
    for i, string in enumerate(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
        rand_int = random.randrange(20)
        in_s += string * rand_int
        out_s += str(i) * rand_int
    assert _solve(in_s) == out_s
