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
        layer = 0
        queue = [(self, layer)]
        while len(queue):
            cur = queue.pop(0)
            cur_node = cur[0]
            cur_layer = cur[1]
            if cur_layer > layer:
                print ('-> ', end='')
                layer = cur_layer
            print (str(cur[0].val), '', end='')
            if cur_node.left:
                queue.append((cur_node.left, cur_layer + 1))
            if cur_node.right:
                queue.append((cur_node.right, cur_layer + 1))
        print ()

    def print_tree_in_order(self):
        """In-Order Traversal."""
        if self.left:
            self.left.print_tree()
        print (str(self.val) + ' -> ', end='')
        if self.right:
            self.right.print_tree()
        print ('End')

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
        nodes = [None if val == 'null' else cls(int(val))
                 for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root
