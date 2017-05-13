# coding=utf-8

"""Minimum Absolute Difference in BST."""

from TreeNode import TreeNode


# 比较奇怪的是速度是递减的，也就是 NlgN 最快的
# 这是适用于任何 Tree 的 NlgN 解法
def _get_minimum_difference(root):
    stack = []

    def _add(cur):
        if cur:
            stack.append(cur.val)
            _add(cur.left)
            _add(cur.right)

    _add(root)
    stack.sort()
    length = len(stack)
    ans = 0 if length == 1 or length == 0 else 0x7fffffff
    for i in xrange(1, length):
        difference = stack[i] - stack[i - 1]
        if difference < ans:
            ans = difference
    return ans


# In order Traverse: BST 有序排列
class Solution(object):

    def get_minimum_difference(self, root):
        """Return abs minimum difference."""
        self._minimum_difference = 0x7fffffff
        self._prev = -1

        def _in_order_traverse(self, cur):
            if cur:
                _in_order_traverse(self, cur.left)
                if self._prev != -1:
                    self._minimum_difference = min(
                        self._minimum_difference, cur.val - self._prev)
                self._prev = cur.val
                _in_order_traverse(self, cur.right)

        _in_order_traverse(self, root)
        return self._minimum_difference


# 一种不使用中序遍历但是使用了 BST 性质的方法，就是传递上下界给每个节点
def _get_minimum_difference3(root):

    def _helper(cur, lower_bound, upper_bound):
        if cur:
            return min(cur.val - lower_bound,
                       upper_bound - cur.val,
                       _helper(cur.left, lower_bound, cur.val),
                       _helper(cur.right, cur.val, upper_bound))
        else:
            return 0xfffffff

    return _helper(root, -0xfffffff, 0xfffffff)


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(5)
    node1.right = node3
    node3.left = node2
    print (_get_minimum_difference(node1))
    print (Solution().get_minimum_difference(node1))
    print (_get_minimum_difference3(node1))
