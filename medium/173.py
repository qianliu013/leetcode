# coding=utf-8

"""Binary Search Tree Iterator."""


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.__stack = []
        self.__add_all_left(root)

    def __add_all_left(self, node):
        while node:
            self.__stack.append(node)
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.__stack) > 0

    def next(self):
        """
        :rtype: int
        """
        res = self.__stack.pop()
        self.__add_all_left(res.right)
        return res.val
