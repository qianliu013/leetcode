# coding=utf-8

"""Average of Levels in Binary Tree."""


def _solve(root):
    ans = []

    def _depth(cur, row):
        if cur:
            if len(ans) <= row:
                ans.append([cur.val])
            else:
                ans[row].append(cur.val)
            _depth(cur.left, row + 1)
            _depth(cur.right, row + 1)
    _depth(root, 0)
    return [sum(arr) * 1.0 / len(arr) for arr in ans]


def _solve1(root):
    ans, level = [], [root]
    while level:
        ans.append(sum(node.val for node in level) * 1.0 / len(level))
        level = [kid for node in level for kid in (node.left, node.right) if kid]
    return ans
