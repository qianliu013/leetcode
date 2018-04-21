# coding=utf-8
"""Lowest Common Ancestor of a Binary Tree."""


# 时间复杂度为 O(n)
# 对于有 q 个查询序列的离线 LCA 问题，存在 O(n + q) 的方法（Tarjan 算法）
def _solve(root, p, q):
    def _dfs(cur):
        if not cur:
            return
        if cur == p or cur == q:
            return cur
        left, right = _dfs(cur.left), _dfs(cur.right)
        if left and right:
            return cur
        else:
            return left or right

    return _dfs(root)
