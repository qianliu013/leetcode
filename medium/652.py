# coding=utf-8
"""Find Duplicate Subtrees.

>>> solve = _solve
"""


def _solve(root):
    res = {}

    # postorder 与此类似，inorder 不能这样做，如当树的结果是 [0,0,0,0,null,null,0,null,null,null,0]
    # inorder 遍历就有问题
    def _preorder(node):
        if node is None:
            return '#'
        node_str = '{},{},{}'.format(node.val, _preorder(node.left), _preorder(node.right))
        if node_str in res:
            res[node_str] = node
        else:
            res[node_str] = None
        return node_str

    def _inorder(node):
        if node is None:
            return ''
        node_str = '({}{}{})'.format(_inorder(node.left), node.val, _inorder(node.right))
        if node_str in res:
            res[node_str] = node
        else:
            res[node_str] = None
        return node_str

    # _preorder(root)
    _inorder(root)
    return [val for val in res.values() if val]


# python 使用 tuple 做 key 需要注意的地方可参考
# https://discuss.leetcode.com/topic/97625/o-n-time-and-space-lots-of-analysis
