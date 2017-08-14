# coding=utf-8

"""Two Sum IV - Input is a BST."""


def _solve(root, k):
    nums = []

    def _dfs(root):
        if root.left:
            _dfs(root.left)
        nums.append(root.val)
        if root.right:
            _dfs(root.right)
    _dfs(root)
    left, right = 0, len(nums) - 1
    while left < right:
        two_sum = nums[left] + nums[right]
        if two_sum == k:
            return True
        if two_sum < k:
            left += 1
        else:
            right -= 1
    return False


def _solve1(root, k):
    res = set()

    def _find(root):
        if not root:
            return False
        if k - root.val in res:
            return True
        res.add(root.val)
        return _find(root.left) or _find(root.right)
    return _find(root)
