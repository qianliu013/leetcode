"""Tree Node Class."""

from __future__ import print_function


class TreeNode(object):
    """Definition for a binary tree node."""

    def __init__(self, x):
        """Init node."""
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        """Print node val instead of origin val."""
        return str(self.val)

    def print_tree(self):
        """Print Tree."""
        queue = [[self]]
        while queue[-1]:
            queue.append([child for node in queue[-1] if node for child in (node.left, node.right)])
        print(queue[:-2])

    def print_tree_in_order(self):
        """In-Order Traversal."""
        if self.left:
            self.left.print_tree()
        print(str(self.val) + ' -> ', end='')
        if self.right:
            self.right.print_tree()
        print('End')

    def get_depth(self):
        """Get the depth of node."""
        left_depth = self.left.get_depth() if self.left else 0
        right_depth = self.right.get_depth() if self.right else 0
        return max(left_depth, right_depth) + 1

    @classmethod
    def de_serialize(cls, string):
        """Build a tree from the string."""
        if string == '{}':
            return None
        nodes = [
            None if val == 'null' else cls(int(val)) for val in string.strip('[]{}').split(',')
        ]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root
