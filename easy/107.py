# coding=utf-8

"""Binary Tree Level Order Traversal II."""

from __future__ import print_function
from TreeNode import TreeNode


# 这里写的略有点麻烦
def _solve(root):
    if not root:
        return []
    layer = 0
    ans = []
    layer_nodes = []
    queue = [(root, layer)]
    while len(queue):
        cur = queue.pop(0)
        cur_node = cur[0]
        cur_layer = cur[1]
        if cur_layer > layer:
            layer = cur_layer
            ans.append([node.val for node in layer_nodes])
            layer_nodes = [cur_node]
        else:
            layer_nodes.append(cur_node)
        if cur_node.left:
            queue.append((cur_node.left, cur_layer + 1))
        if cur_node.right:
            queue.append((cur_node.right, cur_layer + 1))
    ans.append([node.val for node in layer_nodes])
    return ans[::-1]


if __name__ == '__main__':
    print (_solve(None))
    print (_solve(TreeNode(1)))
    tree = TreeNode.de_serialize('[3,9,20,null,null,15,7]')
    print (_solve(tree))
