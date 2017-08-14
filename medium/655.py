# coding=utf-8

"""Print Binary Tree.

>>> solve = _solve
>>> solve()

"""


def _solve(root):
    def _compute_depth(root):
        return 1 + max(_compute_depth(root.left), _compute_depth(root.right)) if root else 0
    depth = _compute_depth(root)
    width = (1 << depth) - 1
    ans = [[""] * width for _ in xrange(depth)]

    def _dfs(root, pos, cur_depth):
        if root:
            half_width = (1 << (depth - cur_depth - 1)) / 2
            ans[cur_depth][pos] = str(root.val)
            _dfs(root.left, pos - half_width, cur_depth + 1)
            _dfs(root.right, pos + half_width, cur_depth + 1)

    _dfs(root, width / 2, 0)
    return ans


from TreeNode import TreeNode
print _solve(TreeNode.de_serialize('[1, 2]'))
print _solve(TreeNode.de_serialize('[1,2,5,3,null,null,null,4]'))
