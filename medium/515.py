# coding=utf-8

"""Find Largest Value in Each Tree Row.

>>> from TreeNode import TreeNode
>>> root = TreeNode.de_serialize('[1,3,2,5,3,null,9]')
>>> solve = _solve1
>>> solve(None)
[]
>>> solve(root)
[1, 3, 9]
"""


# dfs
def _solve(root):
    ans = []

    def _depth(cur, row):
        if cur:
            if len(ans) <= row:
                ans.append(cur.val)
            else:
                ans[row] = max(ans[row], cur.val)
            _depth(cur.left, row + 1)
            _depth(cur.right, row + 1)
    _depth(root, 0)
    return ans


# bfs
def _solve1(root):
    ans, row = [], [root]
    while any(row):
        ans.append(max(node.val for node in row))
        row = [child for node in row for child in (node.left, node.right) if child]
    return ans


# 来自 : https://discuss.leetcode.com/topic/81321/1-liner-python-divide-and-conquer
# 注意 map 的使用
def largestValues(self, root):
    return [root.val] + map(max, *map(self.largestValues, (root.left, root.right))) if root else []
