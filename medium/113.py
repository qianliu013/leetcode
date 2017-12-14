# coding=utf-8

"""Path Sum II."""


def _solve(root, sum):
    res = []

    def _dfs(node, path, path_sum):
        if node:
            if node.left or node.right:
                _dfs(node.left, path + [node.val], path_sum + node.val)
                _dfs(node.right, path + [node.val], path_sum + node.val)
            elif path_sum + node.val == sum:
                res.append(path + [node.val])

    _dfs(root, [], 0)
    return res


def _solve1(root, sum):
    res, path = [], []

    def _dfs(node, remaining):
        if node:
            path.append(node.val)
            if not node.left and not node.right and node.val == remaining:
                res.append(list(path))
            else:
                _dfs(node.left, remaining - node.val)
                _dfs(node.right, remaining - node.val)
            path.pop()
    _dfs(root, sum)
    return res
