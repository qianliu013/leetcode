# coding=utf-8

"""Path Sum."""

from TreeNode import TreeNode


def _solve(root, sum):
    def _help(root, cur):
        if root:
            if not root.left and not root.right:
                return cur + root.val == sum
            else:
                return _help(root.left, cur + root.val) or _help(root.right, cur + root.val)
        else:
            return False
    return _help(root, 0) if root else False


if __name__ == '__main__':
    # ROOT = TreeNode.de_serialize('[1,2]')
    # print _solve(ROOT, 1)
    ROOT = TreeNode.de_serialize('[5,4,8,11,null,13,4,7,2,null,null,null,1]')
    print _solve(ROOT, 22)
    # print _solve(None, 1)
    # print _solve(None, 0)
