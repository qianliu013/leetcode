# coding=utf-8
"""Pyramid Transition Matrix.

>>> solve = _solve
>>> solve('XYZ', ['XYD', 'YZE', 'DEA', 'FFF'])
True
"""

import collections


def _solve(bottom, allowed):
    to_nxt = collections.defaultdict(list)
    for triple in allowed:
        to_nxt[triple[:2]].append(triple[2])

    def _dfs(cur):
        if len(cur) == 1:
            return True
        all_nxt = []
        for i in xrange(len(cur) - 1):
            all_nxt.append(to_nxt[cur[i:i + 2]])
        all_pro = reduce(lambda acc, cur: acc * len(cur), all_nxt, 1)
        for idx in xrange(all_pro):
            nxt = ''
            for j in xrange(len(all_nxt)):
                nxt += all_nxt[j][idx % len(all_nxt[j])]
                idx /= len(all_nxt[j])
            if _dfs(nxt):
                return True
        return False

    return _dfs(bottom)
