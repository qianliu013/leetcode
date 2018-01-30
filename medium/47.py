# coding=utf-8
"""Permutations II.

>>> solve = _solve
>>> len(solve([1, 1, 2, 2, 3, 4, 4]))
630
"""


# 从数组中取一个元素成为新数组第一个，然后从剩下的元素中取第二个
# 这种做法重要考虑的是：同一个位置相同数字只能取一次
# 一种比较简单的思路：每次递归都遍历一次数组，但是排除已经选好的数
# 代码参考自：https://discuss.leetcode.com/topic/31445/really-easy-java-solution-much-easier-than-the-solutions-with-very-high-vote
def _solve(nums):
    res, length = [], len(nums)
    used = [False] * length
    nums.sort()

    def _dfs(cur):
        if len(cur) == length:
            res.append(cur)
        else:
            for i in xrange(length):
                if not used[i]:
                    if i > 0 and nums[i - 1] == nums[i] and not used[i - 1]:
                        continue
                    used[i] = True
                    _dfs(cur + [nums[i]])
                    used[i] = False

    _dfs([])
    return res


# 可以避免每次去遍历整个数组，可以每次交换数到第一个，然后从下一个下标开始，避免重复的方法有
# - 可以使用 set 来保证数字的唯一性
# - 保证子数组的有序性
def _solve1(nums):
    nums.sort()
    res = []

    def _dfs(path, nums):
        if nums:
            for i, _ in enumerate(nums):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                _dfs(path + [nums[i]], nums[:i] + nums[i + 1:])
        else:
            res.append(path)

    _dfs([], nums)
    return res


# 循环求解，代码来自
# https://discuss.leetcode.com/topic/32976/9-line-python-solution-with-1-line-to-handle-duplication-beat-99-of-others
def _solve2(nums):
    ans = [[]]
    for num in nums:
        ans = [l[:i] + [num] + l[i:] for l in ans for i in xrange((l + [num]).index(num) + 1)]
    return ans


# 直接使用 31 Next Permutation 的思路可得到结果
def _solve3(nums):
    nums.sort()
    res, length = [list(nums)], len(nums)
    i = length - 1
    while True:
        for i in xrange(length - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                break
        else:
            break
        for j in xrange(length - 1, i - 1, -1):
            if nums[j] > nums[i - 1]:
                break
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        nums[i:] = nums[i:][::-1]
        res.append(list(nums))
    return res
