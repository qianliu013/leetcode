# coding=utf-8

"""Binary Tree Inorder Traversal."""


def _solve(root):
    node, stack, ans = root, [], []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        ans.append(node.val)
        node = node.right
    return ans


# Morris traversal
def _solve1(root):
    res, cur = [], root
    while cur:
        if cur.left:
            predecessor = cur.left
            while predecessor.right and predecessor.right != cur:
                predecessor = predecessor.right
            if predecessor.right:
                predecessor.right = None
                res.append(cur.val)
                cur = cur.right
            else:
                predecessor.right = cur
                cur = cur.left
        else:
            res.append(cur.val)
            cur = cur.right
    return res
