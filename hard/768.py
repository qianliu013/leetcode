# coding=utf-8
"""Max Chunks To Make Sorted II.

>>> solve = _solve
>>> solve([4, 3, 2, 1, 0])
1
>>> solve([1, 0, 2, 3, 4])
4
>>> solve([2, 1, 3, 4, 4, 5])
5
>>> solve([1, 1, 0, 0, 1])
2
"""


# 使用 sort 的方法：比较原数组和排序后数组的区别
# - 考虑结果数组和原数组的数的对应的位置：可以使用下标记录每个数的位置（`sorted` 是稳定排序）
def _solve(arr):
    sorted_arr = sorted([(num, i) for i, num in enumerate(arr)])
    ans = max_i = 0
    for i, _ in enumerate(arr):
        max_i = max(max_i, sorted_arr[i][1])
        if max_i == i:
            ans += 1
    return ans


# - 一种直接的思路：使用 dict 依次比较内容，如果内容（不考虑顺序）是一致的，就意味着构成一个 chunk
#   可以用滑动窗口记录差距的数量：https://leetcode.com/articles/max-chunks-to-make-sorted-ii/
#   方便的 python Counter 直接比较也可以：https://discuss.leetcode.com/topic/117878/python-easy-and-concise-solution


# - 比较前缀和，代码来自：https://discuss.leetcode.com/topic/118747/c-9-lines-15ms
def _solve1(arr):
    sum1 = sum2 = ans = 0
    sorted_arr = sorted(arr)
    for i in xrange(len(arr)):
        sum1 += arr[i]
        sum2 += sorted_arr[i]
        ans += sum1 == sum2
    return ans


# O(n) 的方法：预处理数组，保证某段的内容合理：这一段最大的数小于等于右面最小的数
# 代码参考自：https://discuss.leetcode.com/topic/117875/java-solution-left-max-and-right-min
def _solve2(arr):
    length = len(arr)
    max_left, min_right = [arr[0]] + [0] * (length - 1), [0] * (length - 1) + [arr[-1]]
    for i in xrange(1, length):
        max_left[i] = max(max_left[i - 1], arr[i])
    for i in xrange(length - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], arr[i])
    return sum(max_left[i] <= min_right[i + 1] for i in xrange(length - 1)) + 1
