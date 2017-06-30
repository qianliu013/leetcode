# coding=utf-8

"""Convert BST to Greater Tree. """


from TreeNode import TreeNode


def _solve(root):
    greater = [0]

    def _in_order(cur):
        if cur:
            _in_order(cur.right)
            cur.val += greater[0]
            greater[0] = cur.val
            _in_order(cur.left)
    _in_order(root)
    return root


_solve(TreeNode.de_serialize('[5,2,8,1,3,6,9]')).print_tree()
