# coding=utf-8
"""Flatten Binary Tree to Linked List.

>>> solve = _solve
"""


# 我的思路是：对于一颗树， flatten 左子树，flattten 右子树，然后连接，返回整棵树的前序遍历的最后一个节点
# 下面解法的一种变种，即一种无返回值的、较为容易理解的思路是，flatten 左右子树后，主动去寻找左子树的最后节点，连接
def _solve(root):
    def _flatten(node):
        if node:
            left, right = _flatten(node.left), _flatten(node.right)
            if left:
                node.left, node.right, left.right = None, node.left, node.right
            return right or left or node
        return None

    _flatten(root)


# 非递归解法：寻找左子树的最后节点，然后连接，继续处理新的右子树
# 代码参考自：https://discuss.leetcode.com/topic/3995/share-my-simple-non-recursive-solution-o-1-space-complexity
def _solve1(root):
    cur = root
    while cur:
        if cur.left:
            prev = cur.left
            while prev.right:
                prev = prev.right
            cur.left, cur.right, prev.right = None, cur.left, cur.right
        cur = cur.right


# 一种完全不同递归思路：反向前序遍历；访问顺序中当前节点的右子树总是赋予之前已 flatten 的树
# 代码参考自：https://discuss.leetcode.com/topic/11444/my-short-post-order-traversal-java-solution-for-share
def _solve2(root):
    def _flatten(cur, prev):
        if not cur:
            return prev
        prev = _flatten(cur.right, prev)
        prev = _flatten(cur.left, prev)
        cur.left, cur.right, prev = None, prev, cur
        return prev

    _flatten(root, None)


# 另一种非递归思路：用 stack 帮助我们将节点顺序整理成最终的形式
# 代码参考自：https://discuss.leetcode.com/topic/5783/accepted-simple-java-solution-iterative
def _solve3(root):
    if not root:
        return root
    stack = [root]
    while stack:
        cur = stack.pop()
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
        if stack:
            cur.right = stack[-1]
        cur.left = None
