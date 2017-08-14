# coding=utf-8

"""Maximum Binary Tree."""

from TreeNode import TreeNode


def _solve(nums):
    if not nums:
        return None

    def _dfs1(root, index):
        if root.val > index:
            if root.left:
                _dfs1(root.left, index)
            else:
                root.left = TreeNode(index)
        else:
            if root.right:
                _dfs1(root.right, index)
            else:
                root.right = TreeNode(index)

    def _dfs2(root):
        if root:
            root.val = nums[root.val]
            _dfs2(root.left)
            _dfs2(root.right)

    res = sorted([(num, i) for i, num in enumerate(nums)], reverse=True)
    root = TreeNode(res[0][1])
    for _, index in res[1:]:
        _dfs1(root, index)
    _dfs2(root)
    return root


def _solve1(nums):
    def _compute_max_i(left, right):
        ans = left
        for i in xrange(left, right):
            if nums[ans] < nums[i]:
                ans = i
        return ans

    def _construct(left, right):
        if left == right:
            return None
        max_i = _compute_max_i(left, right)
        root = TreeNode(nums[max_i])
        root.left = _construct(left, max_i)
        root.right = _construct(max_i + 1, right)
        return root

    return _construct(0, len(nums))


# 也可以不记录最大值，不使用递归，直接模拟插入
# 参考 https://discuss.leetcode.com/topic/98509/c-o-n-solution，但最坏情况下复杂度并不是 O(n)
def _solve2(nums):
    stack = []
    for num in nums:
        cur = TreeNode(num)
        while stack and stack[-1].val < num:
            cur.left = stack.pop()
        if stack:
            stack[-1].right = cur
        stack.append(cur)
    return stack[0]
