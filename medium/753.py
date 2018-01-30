# coding=utf-8
"""Open the Lock.

>>> solve = _solve
>>> solve(["0201", "0101", "0102", "1212", "2002"], "0202")
6
>>> solve(["8888"], "0009")
1
>>> solve(["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"], "8888")
-1
>>> solve(["0000"], "8888")
-1
"""


# 双向 BFS 要比单向快很多
def _solve(deadends, target):
    visited = set(deadends)
    begin, end = set(['0000']), set([target])
    step = 0
    nxt_char = {str(i): [str((i + 1) % 10), str((i + 9) % 10)] for i in xrange(10)}
    while begin and end:
        if len(begin) > len(end):
            begin, end = end, begin
        tmp = set()
        for node in begin:
            if node in end:
                return step
            if node not in visited:
                for i in xrange(4):
                    new_nodes = [node[:i] + nxt + node[i + 1:] for nxt in nxt_char[node[i]]]
                    tmp.add(new_nodes[0])
                    tmp.add(new_nodes[1])
                visited.add(node)
        step += 1
        begin = tmp
    return -1
