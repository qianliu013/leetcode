# coding=utf-8

"""Delete Node in a BST.

>>> solve = _solve
"""


def _solve(root, key):
    def _update(cur):
        if cur.left.left:
            return _update(cur.left)
        else:
            val = cur.left.val
            cur.left = cur.left.right
            return val

    def _dfs(node):
        if node:
            if node.val == key:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                if node.right.left:
                    node.val = _update(node.right)
                    return node
                else:
                    node.right.left = node.left
                    return node.right

            elif node.val > key:
                node.left = _dfs(node.left)
            else:
                node.right = _dfs(node.right)
        return node
    return _dfs(root)


# 递归思路一种更简洁的写法
def _solve1(root, key):
    def _dfs(node, target):
        if node:
            if node.val == target:
                if node.left is None:
                    return node.right
                if node.right is None:
                    return node.left
                min_node = node.right
                while min_node.left:
                    min_node = min_node.left
                node.val = min_node.val
                node.right = _dfs(node.right, node.val)
            elif node.val > target:
                node.left = _dfs(node.left, target)
            else:
                node.right = _dfs(node.right, target)
        return node
    return _dfs(root, key)


# Iterative 写法只要保存 prev,cur 并判断即可；并不难，但写起来繁琐点
# 具体可参考：https://discuss.leetcode.com/topic/67962/iterative-solution-in-java-o-h-time-and-o-1-space
