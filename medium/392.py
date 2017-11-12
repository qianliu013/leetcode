# coding=utf-8

"""Is Subsequence.

>>> solve = _solve
>>> solve('', 'abc')
True
>>> solve('help', 'hello')
False
"""

import bisect
import collections


def _solve(s, t):
    if s == '':
        return True
    pos = 0
    for ch in t:
        if ch == s[pos]:
            pos += 1
            if pos == len(s):
                return True
    return False


# 另一种思路是从左到右，依次查找 s 中每个字母相对于前一个的最左位置
# 第一眼看起来这种方法似乎是 O(len(s) * len(t)) 的，但是可以预处理得到 t 中每个字母的 index
# 然后使用二分查找寻找位置，这样复杂度就变成了 O(len(t)) + O(len(s) * log(len(t)) )
# 显然这种方法在 follow up 的情况下，速度会快，
# 而前一种方法扩展为 follow up 的方法是将 pos 改为一个数组，依次遍历

def _solve1(s, t):
    pos_map = collections.defaultdict(list)
    for i, ch in enumerate(t):
        pos_map[ch].append(i)
    prev = 0
    for ch in s:
        if ch not in pos_map:
            return False
        ch_indexes = pos_map[ch]
        pos = bisect.bisect_left(ch_indexes, prev)
        if pos == len(ch_indexes):
            return False
        prev = ch_indexes[pos] + 1
    return True
