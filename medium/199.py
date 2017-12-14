# coding=utf-8

"""Binary Tree Right Side View."""


# bfs
def _solve(root):
    res, nodes = [], [root]
    if root:
        while nodes:
            res.append(nodes[-1].val)
            nodes = [kid for node in nodes for kid in (node.left, node.right) if kid]
    return res


# dfs
def _solve1(root):
    res = []

    def _dfs(cur, depth):
        if cur:
            if depth == len(res):
                res.append(cur.val)
            _dfs(cur.right, depth + 1)
            _dfs(cur.left, depth + 1)
    _dfs(root, 0)
    return res
