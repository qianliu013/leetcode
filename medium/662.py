# coding=utf-8

"""Maximum Width of Binary Tree.

>>> solve = _solve
"""


# 此题其他形式的 dfs 以及略加改动 bfs（储存额外的 depth）很容易想到及实现，因而不列了
def _solve(root):
    if not root:
        return 0
    layer, ans = [(root, 1)], 1
    while layer:
        ans = max(layer[-1][1] - layer[0][1] + 1, ans)
        new_layer = []
        for node, i in layer:
            if node.left:
                new_layer.append((node.left, i * 2 - 1))
            if node.right:
                new_layer.append((node.right, i * 2))
        layer = new_layer
    return ans
