# coding=utf-8

"""Binary Tree Paths."""

from TreeNode import TreeNode


def _solve(root):
    ans = []
    if not root:
        return ans

    def _help(root, path):
        if root:
            path += '->' + str(root.val)
            if not root.left and not root.right:
                ans.append(path[2:])
            _help(root.left, path)
            _help(root.right, path)

    _help(root, '')
    return ans


if __name__ == '__main__':
    ROOT = TreeNode.de_serialize('[1,2,3,3,5,12,2]')
    print _solve(ROOT)
    ROOT = TreeNode.de_serialize('[1]')
    print _solve(ROOT)
    print _solve(None)
