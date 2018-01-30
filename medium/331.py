# coding=utf-8
"""Verify Preorder Serialization of a Binary Tree.

>>> solve = _solve1
>>> solve("9,3,4,#,#,1,#,#,2,#,6,#,#")
True
>>> solve('1,#')
False
>>> solve('1,#,#,1')
False
"""


# 用 stack 模拟遍历树
def _solve(preorder):
    stack = []
    nodes = preorder.split(',')
    for node in nodes[:-1]:
        if node != '#':
            stack.append(node)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return nodes[-1] == '#' and not stack


# 其实 stack 也不是必要的，因为 stack 存的东西从来没用过，我们需要的仅是 stack 的 size（即深度）
def _solve1(preorder):
    depth, nodes = 0, preorder.split(',')
    for node in nodes[:-1]:
        if node != '#':
            depth += 1
        else:
            if depth:
                depth -= 1
            else:
                return False
    return nodes[-1] == '#' and depth == 0


# 考虑每个节点的子节点数
def _solve2(preorder):
    to_visit, nodes = 1, preorder.split(',')
    for node in nodes:
        to_visit -= 1
        if to_visit < 0:
            return False
        else:
            to_visit += (node != '#') * 2
    return to_visit == 0
