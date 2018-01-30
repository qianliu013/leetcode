# coding=utf-8
"""Construct Binary Tree from Preorder and Inorder Traversal.

>>> solve = _solve
"""

from TreeNode import TreeNode


# 我的递归思路：按照前序数组建左子树，如果前序数组当前元素等于中序元素，表示 left 到头
# 然后考虑建右子树或者回退，判断依据是前序的下一个节点是否等于其父节点值
def _solve(preorder, inorder):
    length, indexes = len(preorder), [0, 0]

    def _build(father):
        if indexes[0] == length:
            return None
        root = TreeNode(preorder[indexes[0]])

        indexes[0] += 1
        if root.val == inorder[indexes[1]]:
            indexes[1] += 1
        else:
            root.left = _build(root.val)

        if indexes[1] < length and father == inorder[indexes[1]]:
            indexes[1] += 1
        else:
            root.right = _build(father)

        return root

    return _build(None)


# 其实上面的思路非常容易可以改为非递归版本
def _solve1(preorder, inorder):
    if not preorder:
        return None
    stack, i_i = [], 0
    root = cur = TreeNode(preorder[0])
    for num in preorder[1:]:
        if cur.val != inorder[i_i]:
            cur.left = TreeNode(num)
            stack.append(cur)
            cur = cur.left
        else:
            i_i += 1
            while stack and stack[-1].val == inorder[i_i]:
                i_i += 1
                cur = stack.pop()
            cur.right = TreeNode(num)
            cur = cur.right
    return root


# 一种更加常见的递归思路：根据前序节点分隔 inorder 数组
# 当然，具体的写法也很多，下面给出一种参数较少的方法
def _solve2(preorder, inorder):
    if not preorder:
        return None
    i_map, i_pre = {val: i for i, val in enumerate(inorder)}, [0]

    def _build(start, end):
        if start > end or i_pre[0] == len(preorder):
            return None
        root = TreeNode(preorder[i_pre[0]])
        i_pre[0] += 1
        index = i_map[root.val]
        root.left = _build(start, index - 1)
        root.right = _build(index + 1, end)
        return root

    return _build(0, len(preorder) - 1)


# 其实上述方法也可以改为非递归版
def _solve3(preorder, inorder):
    i_map = {val: num for num, val in enumerate(inorder)}
    stack = []
    root = parent = None
    for num in preorder:
        node = TreeNode(num)
        if not root:
            root = node
        elif i_map[num] < i_map[parent.val]:
            parent.left = node
            stack.append(parent)
        elif i_map[num] > i_map[parent.val]:
            while stack and i_map[num] > i_map[stack[-1].val]:
                parent = stack.pop()
            parent.right = node
        parent = node
    return root


if __name__ == '__main__':
    solve = _solve
    solve([3, 2, 1, 4], [1, 2, 3, 4]).print_tree()
    solve([5, 1, 3, 2, 6], [1, 3, 5, 6, 2]).print_tree()
    solve([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]).print_tree()
