# coding=utf-8

"""Permutations."""


def _solve(nums):
    res, length = [], len(nums)

    def _dfs(start):
        if start == length:
            res.append(list(nums))
            return
        for i in xrange(start, length):
            nums[start], nums[i] = nums[i], nums[start]
            _dfs(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    _dfs(0)
    return res


# 参考自 https://discuss.leetcode.com/topic/6377/my-ac-simple-iterative-java-python-solution
# 这种做法的一行写法（使用递归）和其他变形可参考 https://discuss.leetcode.com/topic/17277/one-liners-in-python
def _solve1(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in xrange(len(perm) + 1):
                new_perms.append(perm[:i] + [n] + perm[i:])
        perms = new_perms
    return perms

# 还有一种思路是使用 [Next Permutation](https://leetcode.com/problems/next-permutation/description/)
