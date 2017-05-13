# coding=utf-8

"""Binary Tree Tilt."""

from TreeNode import TreeNode


def _solve(root):
    def _help(root):
        if root:
            left_result = _help(root.left)
            right_result = _help(root.right)
            return (left_result[0] + right_result[0] + abs(left_result[1] - right_result[1]),
                    left_result[1] + right_result[1] + root.val)
        else:
            return 0, 0
    return _help(root)[0]


if __name__ == '__main__':
    root = TreeNode.de_serialize('[1,123,124,12,43,678,123,5678,123]')
    print (_solve(root))
    print (_solve(None))
    print (_solve(TreeNode(1)))
