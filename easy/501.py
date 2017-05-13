# coding=utf-8

"""Find Mode in Binary Search Tree."""

from __future__ import print_function
from TreeNode import TreeNode


def _solve(root):
    result = {}
    max_count = [0]

    def _help(root):
        if root:
            result[root.val] = result.get(root.val, 0) + 1
            max_count[0] = max(max_count[0], result[root.val])
            _help(root.left)
            _help(root.right)

    _help(root)
    return [key for key, val in result.items() if val == max_count[0]]


def _solve1(root):
    ans = []
    result = [None, 0, 0]
    CUR_VAL = 0
    COUNT = 1
    MAX_COUNT = 2

    def _help(root):
        if not root:
            return
        _help(root.left)
        if root.val == result[CUR_VAL]:
            result[COUNT] += 1
        else:
            result[COUNT] = 1
            result[CUR_VAL] = root.val
        if result[MAX_COUNT] < result[COUNT]:
            result[MAX_COUNT] = result[COUNT]
            while len(ans):
                ans.pop()
            ans.append(root.val)
        elif result[MAX_COUNT] == result[COUNT]:
            ans.append(root.val)
        _help(root.right)

    _help(root)
    return ans


if __name__ == '__main__':
    root = TreeNode.de_serialize('[2,null,2,2,1,2,1,1]')
    print (_solve1(root))
