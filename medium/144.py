# coding=utf-8

"""Binary Tree Preorder Traversal.

>>> from TreeNode import TreeNode
>>> solve = _solve
>>> solve(TreeNode.de_serialize('[1,2,3,4,5,6,7]'))
[1, 2, 4, 5, 3, 6, 7]
"""


def _solve(root):
    node, stack, ans = root, [], []
    while node or stack:
        while node:
            ans.append(node.val)
            stack.append(node)
            node = node.left
        node = stack.pop().right
    return ans


def _solve1(root):
    ans, stack = [], [root]
    while stack:
        node = stack.pop()
        if node:
            ans.append(node.val)
            stack.append(node.right)
            stack.append(node.left)
    return ans


# Morris traversal
def _solve2(root):
    res, cur = [], root
    while cur:
        if cur.left:
            predecessor = cur.left
            while predecessor.right and predecessor.right != cur:
                predecessor = predecessor.right
            if predecessor.right:
                predecessor.right = None
                cur = cur.right
            else:
                res.append(cur.val)
                predecessor.right = cur
                cur = cur.left
        else:
            res.append(cur.val)
            cur = cur.right
    return res
