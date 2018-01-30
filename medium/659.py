# coding=utf-8
"""Split Array into Consecutive Subsequences.

>>> solve = _solve
>>> solve([1, 1, 2, 2, 3, 3])
True
>>> solve([1, 2, 3, 3, 4, 5])
True
>>> solve([1, 2, 3, 4, 4, 5])
False
"""

import collections

# 此题其实比较容易想到贪心思路：
# 新增的数总是优先填充以前长度小于 3 的数组，然后多出来优先加入之前长度大于 3 的数组，再有剩余然后开始新数组
# 这个思路也有很多种写法
# 也许会想到使用堆（优先队列）来做，但是其实时间复杂度高且并不是很优雅


#  O(n) time O(1) space
def _solve(nums):
    need0 = need1 = need2 = 0
    prev, i, length = nums[0] - 2, 0, len(nums)
    while i < length:
        count, cur = 0, nums[i]
        while i < length and cur == nums[i]:
            count += 1
            i += 1
        if cur == prev + 1:
            remaining = count - need1 - need2
            if remaining < 0:
                return False
            if remaining > need0:
                need0, need1, need2 = need0 + need1, need2, remaining - need0
            else:
                need0, need1, need2 = remaining + need1, need2, 0
        else:
            if need1 or need2:
                return False
            need0 = need1 = 0
            need2 = count
        prev = cur
    return need1 == need2 == 0


# O(n) time O(n) space
# 代码参考自 solution：https://leetcode.com/articles/split-array-into-consecutive-subsequences/
def _solve1(nums):
    counter = collections.Counter(nums)
    tails = collections.Counter()
    for num in nums:
        if counter[num] == 0:
            continue
        elif tails[num] > 0:
            tails[num] -= 1
            tails[num + 1] += 1
        elif counter[num + 1] > 0 and counter[num + 2] > 0:
            counter[num + 1] -= 1
            counter[num + 2] -= 1
            tails[num + 3] += 1
        else:
            return False
        counter[num] -= 1
    return True


# 还有一类 O(n) time O(n) space 的写法是用队列或数组表示包含当前元素的所有数组
# 如此题 solution 的第一种解法或者
# https://discuss.leetcode.com/topic/99200/python-o-n-straightforward-solution
