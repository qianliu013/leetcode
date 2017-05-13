"""Maximum Depth of Binary Tree."""


def _max_depth(root):
    if root:
        return max(_max_depth(root.left), _max_depth(root.right)) + 1
    else:
        return 0


class _TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


if __name__ == '__main__':
    node = _TreeNode(1)
    node.left = _TreeNode(2)
    node.left.left = _TreeNode(3)
    print (_max_depth(None))
    print (_max_depth(node))
