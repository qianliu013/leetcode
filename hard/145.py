# coding=utf-8

"""Binary Tree Postorder Traversal.

>>> from TreeNode import TreeNode
>>> solve = _solve
>>> solve(TreeNode.de_serialize('[1,2,3,4,5,6,7]'))
[4, 5, 2, 6, 7, 3, 1]
"""

from TreeNode import TreeNode


# 下面的做法是将根节点在栈中换为一个叶子结点
def _solve(root):
    node, stack, ans = root, [], []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        while not node.right:
            ans.append(node.val)
            if not stack:
                return ans
            node = stack.pop()
        stack.append(TreeNode(node.val))
        node = node.right

    return ans


# 如果能想到每次在数组前面插入，会简单很多
# 那么这种做法几乎方法前序是差不多的
def _solve1(root):
    node, stack, ans = root, [root], []
    while stack:
        node = stack.pop()
        if node:
            ans.append(node.val)
            stack.append(node.left)
            stack.append(node.right)
    return ans[::-1]


def _solve2(root):
    node, stack, ans = root, [], []
    while node or stack:
        while node:
            ans.append(node.val)
            stack.append(node)
            node = node.right
        node = stack.pop().left
    return ans[::-1]


# 还有一类写法是判断上次节点与当前节点的关系
# 一种比较容易理解的写法，参考自
# https://discuss.leetcode.com/topic/30632/preorder-inorder-and-postorder-iteratively-summarization/20
def _solve3(root):
    if not root:
        return []
    ans, stack = [], [root]
    cur, prev = root, None
    while stack:
        prev, cur = cur, stack[-1]
        if cur.left and cur.left != prev and cur.right != prev:
            stack.append(cur.left)
        elif cur.right and cur.right != prev:
            stack.append(cur.right)
        else:
            ans.append(stack.pop().val)
    return ans


# 另一种比较容易理解的写法，参考自
# https://discuss.leetcode.com/topic/1695/my-accepted-code-of-binary-tree-postorder-traversal/10
def _solve4(root):
    if not root:
        return []
    ans, stack = [], [root]
    cur, prev = root, None
    while stack:
        prev, cur = cur, stack[-1]
        if ((cur.right and cur.right == prev) or
                (not cur.right and cur.left == prev) or
                (not cur.right and not cur.left)):
            ans.append(stack.pop().val)
            continue
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return ans


# Morris Traversal，解释可参考 http://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html
def _solve5(root):
    dump, ans = TreeNode(0), []
    dump.left = root
    cur = dump

    def _reverse_path(start, end):
        if start != end:
            prev, cur = start, start.right
            while prev != end:
                cur.right, prev, cur = prev, cur, cur.right

    def _reverse_add_path_nodes(start, end):
        _reverse_path(start, end)
        node = end
        while True:
            ans.append(node.val)
            if node == start:
                break
            node = node.right
        _reverse_path(end, start)

    while cur:
        if cur.left:
            predecessor = cur.left
            while predecessor.right and predecessor.right != cur:
                predecessor = predecessor.right
            if predecessor.right:
                _reverse_add_path_nodes(cur.left, predecessor)
                predecessor.right = None
                cur = cur.right
            else:
                predecessor.right = cur
                cur = cur.left
        else:
            cur = cur.right
    return ans


# 此外还有其他思路，如
# https://discuss.leetcode.com/topic/34258/iterative-method-to-do-three-kinds-of-traversal-just-like-recursive-method-only-changing-one-line-code
# https://discuss.leetcode.com/topic/12801/a-real-postorder-traversal-without-reverse-or-insert-4ms/3
