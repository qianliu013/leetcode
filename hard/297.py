# coding=utf-8

"""Serialize and Deserialize Binary Tree."""


from TreeNode import TreeNode


# dfs 可以变化的地方在于
# - 迭代的形式：可以用非递归的方法构造 string
# - deserialize 记录当前位置的方法：如多返回值、next 方法、改变数组（队列）等
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
                return 'n,'
        return _dfs(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        index, values = [-1], data.split(',')

        def _dfs():
            index[0] += 1
            if values[index[0]] == 'n':
                return None
            cur = TreeNode(int(values[index[0]]))
            cur.left = _dfs()
            cur.right = _dfs()
            return cur

        return _dfs()
