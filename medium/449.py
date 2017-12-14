# coding=utf-8

"""Serialize and Deserialize BST."""

from TreeNode import TreeNode


# 注意与 297 Serialize and Deserialize Binary Tree 不同的地方在于是一棵 BST，因此可以节省内存
# 一般来说，只记录数字+分隔符就行，而如果使用 C/C++ 也可以使得固定数字对应的字符串长度，代码可参考
# https://discuss.leetcode.com/topic/79949/concise-c-19ms-solution-beating-99-4
class Codec(object):

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def _dfs(cur):
            if cur:
                return str(cur.val) + ',' + _dfs(cur.left) + _dfs(cur.right)
            else:
                return ''
        return _dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nums = [int(num) for num in data.split(',')[:-1]]

        def _dfs(left, right):
            if left < right:
                mid = left + 1
                while mid < right and nums[mid] < nums[left]:
                    mid += 1
                root = TreeNode(nums[left])
                root.left, root.right = _dfs(left + 1, mid), _dfs(mid, right)
                return root
            return None

        return _dfs(0, len(nums))


# deserialize 通常是根据中间节点值分别构造左右子树，其实也可以结合 preorder 来做
# 具体代码可参考：https://discuss.leetcode.com/topic/66318/deserialize-from-preorder-and-computed-inorder-reusing-old-solution
