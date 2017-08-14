# coding=utf-8

"""Judge Route Circle."""

import collections


def _solve(moves):
    result = collections.Counter(moves)
    return result['U'] == result['D'] and result['R'] == result['L']
