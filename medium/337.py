# coding=utf-8

"""House Robber III."""

from TreeNode import TreeNode


def _solve(root):
    def _dfs(cur):
        if cur:
            left, right = _dfs(cur.left), _dfs(cur.right)
            return cur.val + left[1] + right[1], max(left) + max(right)
        else:
            return 0, 0
    return max(_dfs(root))


assert _solve(TreeNode.de_serialize('[3,2,3,null,3,null,1]')), 7
assert _solve(TreeNode.de_serialize('[3,4,5,1,3,null,1]')), 9
