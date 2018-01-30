# coding=utf-8

"""Kth Largest Element in an Array.

>>> solve = _solve3
>>> [solve([3, 5, 2, 6, 1, 4], i) for i in range(1, 7)] == range(1, 7)[::-1]
True
"""

# 此题使用 heap 方式较简单，不列出代码，只列出 quick select 的几种方式
# quick select 的思想不难理解，但是原地 partition 的有些写法有点容易出错
# 虽然速度比 `sorted(nums)[-k]` 这行语句要慢


import random


# 一左一右 index 分别表示排序好的左右数组范围
# 下面这种 while 里面套两个 while 的方式其实很容易写错，出错点包括 `<` 和 `<=` 的使用，边界的判断
# 其另一种实现方式可见： https://discuss.leetcode.com/topic/14597/solution-explained
def _solve(nums, k):
    random.shuffle(nums)
    k = len(nums) - k

    def _nth(left, right):
        i, j = left + 1, right
        while True:
            while i <= j and nums[i] < nums[left]:
                i += 1
            while i <= j and nums[left] <= nums[j]:
                j -= 1
            if i >= j:
                break
            nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[j] = nums[j], nums[left]
        if j == k:
            return nums[j]
        if k < j:
            return _nth(left, j - 1)
        else:
            return _nth(j + 1, right)

    return _nth(0, len(nums) - 1)


# 上述代码感觉要注意的细节多，容易写错，因此下面列出多种实现方法
# 思路类似但是在 while 循环里只进行判断，代码参考自：
# https://discuss.leetcode.com/topic/15256/4-c-solutions-using-partition-max-heap-priority_queue-and-multiset-respectively
def _solve1(nums, k):
    def _partition(left, right):
        pivot, i, j = nums[left], left + 1, right
        while i <= j:
            if nums[i] > pivot and nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            if nums[i] <= pivot:
                i += 1
            if nums[j] >= pivot:
                j -= 1
        nums[left], nums[j] = nums[j], nums[left]
        return j

    random.shuffle(nums)
    left, right, k = 0, len(nums) - 1, len(nums) - k
    while True:
        pos = _partition(left, right)
        if pos == k:
            return nums[pos]
        if pos > k:
            right = pos - 1
        else:
            left = pos + 1


# 以 right 为 pivot，不断把大于pivot 换到右面，代码参考自：
# https://discuss.leetcode.com/topic/18662/ac-clean-quickselect-java-solution-avg-o-n-time
def _solve2(nums, k):
    def _partition(left, right):
        pivot, i, j = nums[right], left, right
        while i < j:
            if nums[i] > pivot:
                j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        nums[right], nums[j] = nums[j], nums[right]
        return j

    random.shuffle(nums)
    left, right, k = 0, len(nums) - 1, len(nums) - k
    while True:
        pos = _partition(left, right)
        if pos == k:
            return nums[pos]
        if pos > k:
            right = pos - 1
        else:
            left = pos + 1


# 我认为最有优雅、简洁的写法
# 以 right 为 pivot，不断把小于等于pivot 的数换到左面，代码参考自：
# https://discuss.leetcode.com/topic/29537/concise-java-solution-based-on-quick-select
def _solve3(nums, k):
    def _partition(left, right):
        pivot, nxt = nums[right], left
        for i in xrange(left, right):
            if nums[i] <= pivot:
                nums[i], nums[nxt] = nums[nxt], nums[i]
                nxt += 1
        nums[right], nums[nxt] = nums[nxt], nums[right]
        return nxt

    random.shuffle(nums)
    left, right, k = 0, len(nums) - 1, len(nums) - k
    while True:
        pos = _partition(left, right)
        if pos == k:
            return nums[pos]
        if pos > k:
            right = pos - 1
        else:
            left = pos + 1
