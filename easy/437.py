# coding=utf-8

"""Path Sum III."""

from __future__ import print_function
from TreeNode import TreeNode


def _solve(root, sum):
    ans = [0]

    def _deep(node, result):
        if not node:
            return None
        cur_result = {}
        if node.val == sum:
            ans[0] += 1
        for val, count in result.items():
            cur_sum = val + node.val
            if cur_sum == sum:
                ans[0] += count
            cur_result[cur_sum] = count
        cur_result[node.val] = cur_result.get(node.val, 0) + 1
        _deep(node.left, cur_result)
        _deep(node.right, cur_result)

    result = {}
    _deep(root, result)
    return ans[0]


def _solve1(root, sum):
    def _helper(root, cur_sum):
        if root:
            cur_sum = cur_sum + root.val
            ans = pre_sum.get(cur_sum - target, 0)
            pre_sum[cur_sum] = pre_sum.get(cur_sum, 0) + 1
            ans += _helper(root.left, cur_sum)
            ans += _helper(root.right, cur_sum)
            pre_sum[cur_sum] -= 1
            return ans
        else:
            return 0

    pre_sum = {0: 1}
    target = sum
    return _helper(root, 0)


if __name__ == '__main__':
    node = TreeNode.de_serialize("[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1")
    print (_solve1(node, 4))
    print (_solve1(TreeNode.de_serialize('[1,2,null,3,null,4,null,5]'), 9))
