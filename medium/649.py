# coding=utf-8
"""Dota2 Senate.

>>> solve = _solve
>>> solve('RD')
'Radiant'
>>> solve('RDD')
'Dire'
>>> solve('DDRRRDR')
'Radiant'
>>> solve('DDRRR')
'Dire'
"""

import collections


# 贪心策略是 ban 掉下一个最近的不同阵营元素，因此这道题的方法就是模拟
# 最容易想到的模拟是用数组模拟，不改变长度，改变需要改变的数组元素内容，使之无效
# 每次 ban 都是遍历数组寻找下一个不同阵营的元素
# 更好的模拟方法可以是 1. 使用队列模拟； 2. 不断构建新字符串模拟
# 一个变数是使用一个元素来表示整个阵营还是两个元素来分别表示；其中后者要简单些
def _solve(senate):
    d_minus_r, length = 0, 0
    while len(senate) != length:
        length, new_senate = len(senate), ''
        for senator in senate:
            if senator == 'D':
                if d_minus_r >= 0:
                    new_senate += 'D'
                d_minus_r += 1
            else:
                if d_minus_r <= 0:
                    new_senate += 'R'
                d_minus_r -= 1
        senate = new_senate
    return 'Radiant' if senate[0] == 'R' else 'Dire'


# 代码参考自：https://discuss.leetcode.com/topic/97651/straightforward-and-simple-python
def _solve1(senate):
    length, party = len(senate), collections.defaultdict(collections.deque)
    for i, senator in enumerate(senate):
        party[senator].append(i)
    while party['R'] and party['D']:
        if party['R'][0] < party['D'][0]:
            party['R'].append(party['R'].popleft() + length)
            party['D'].popleft()
        else:
            party['D'].append(party['D'].popleft() + length)
            party['R'].popleft()
    return 'Radiant' if party['R'] else 'Dire'


# 代码参考自：https://leetcode.com/articles/dota2-senate/
def _solve2(senate):
    queue = collections.deque()
    party, bans = [0, 0], [0, 0]
    for senator in senate:
        idx = senator == 'R'
        party[idx] += 1
        queue.append(idx)
    while all(party):
        idx = queue.popleft()
        if bans[idx]:
            bans[idx] -= 1
            party[idx] -= 1
        else:
            bans[idx ^ 1] += 1
            queue.append(idx)
    return 'Radiant' if party[1] else 'Dire'
