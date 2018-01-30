# coding=utf-8
"""Partition to K Equal Sum Subsets.

>>> solve = _solve2
>>> solve([3522, 181, 521, 515, 304, 123, 2512, 312, 922, 407, 146, 1932, 4037, 2646, 3871, 269], 5)
True
>>> solve([5, 3, 1], 3)
False
>>> solve([6, 14, 7, 3, 10, 16, 4], 3)
True
"""


# dfs 方法要注意的是需要反向排序，此是为了减枝，减少一开始搜索子空间
# 每个数必须归属到一个子集中，根据此规则 dfs
def _solve(nums, k):
    the_sum = sum(nums)
    if the_sum % k != 0:
        return False
    nums.sort(reverse=True)
    ave = the_sum / k

    def _dfs(cur, start):
        if k == len(cur) and cur == [ave] * k:
            return True
        for i in xrange(len(cur)):
            if cur[i] + nums[start] <= ave:
                origin = cur[i]
                cur[i] += nums[start]
                if _dfs(cur, start + 1):
                    return True
                cur[i] = origin
        if len(cur) < k and nums[start] <= ave:
            if _dfs(cur + [nums[start]], start + 1):
                return True
        return False

    return _dfs([], 0)


# 一种更常见 dfs 思路：从数组中先得到一组可以构成 target 的 subset，然后下一组；此方法要快一些
def _solve1(nums, k):
    if k == 1:
        return True
    length = len(nums)
    if k > length:
        return False
    total = sum(nums)
    if total % k:
        return False
    target = total / k
    visit = [0] * length
    nums.sort(reverse=True)

    def dfs(k, start, cur_sum):
        if k == 1:
            return True
        if cur_sum == target:
            return dfs(k - 1, 0, 0)
        for i in range(start, length):
            if not visit[i] and cur_sum + nums[i] <= target:
                visit[i] = 1
                if dfs(k, i + 1, cur_sum + nums[i]):
                    return True
                visit[i] = 0
        return False

    return dfs(k, 0, 0)


# 下面这两种 dp 想法来自 solution，虽然速度并不快，然而是可以帮助很好的拓宽思路
# 首先记忆化搜索，1 <= k <= len(nums) <= 16，可以使用 [0, 1<<len(nums)) 中每个数的每一位来表示当前数字是否用过
# 与 _solve1 解法类似，先考虑构成一个 target(average) 的情况，然后第二个，依次类推
# (todo - 1) % target + 1 表示的就是构成当前 target 剩余的数；如果 todo 是 target 的倍数，那么刚好是 target，否则是 todo % target
# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solution/
def _solve2(nums, k):
    target, rem = divmod(sum(nums), k)
    if rem or max(nums) > target:
        return False
    memo = [None] * (1 << len(nums))
    memo[-1] = True

    def _dfs(used, todo):
        if memo[used] is None:
            need = (todo - 1) % target + 1
            memo[used] = any(
                _dfs(used | (1 << i), todo - num) for i, num in enumerate(nums)
                if num <= need and (used & (1 << i)) == 0)
        return memo[used]

    return _dfs(0, k * target)


# 接下来，考虑如何把上述记忆化搜索改为一般的循环 dp
def _solve3(nums, k):
    nums.sort()
    target, rem = divmod(sum(nums), k)
    if rem or nums[-1] > target:
        return False
    length = 1 << len(nums)
    dp = [False] * length
    dp[0] = True
    total = [0] * length

    for state in xrange(length):
        if not dp[state]:
            continue
        for i, num in enumerate(nums):
            nxt = state | (1 << i)
            if not dp[nxt] and nxt != state:
                if num <= target - total[state] % target:
                    total[nxt] = total[state] + num
                    dp[nxt] = True
                else:
                    break
    return dp[-1]
