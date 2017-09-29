# coding=utf-8

"""Top K Frequent Elements.

>>> solve = _solve
>>> solve([1, 1, 2, 3, 2], 2)
[1, 2]
"""

import collections
import heapq

# 不变的都是用 map 来存储数字和出现的次数，变的是如何对获得的结果排序
# 除了下面的方法，你也可以直接对结果排序
# 可以使用改动过的快排（只排序前 k 个）来优化


# O(n lg k)，参考 https://stackoverflow.com/questions/29240807/python-collections-counter-most-common-complexity
# most_common 使用了 heapq 求最大
def _solve(nums, k):
    return [pair[0] for pair in collections.Counter(nums).most_common(k)]


# 优先队列
def _solve2(nums, k):
    res, ans = [], []
    for num, freq in collections.Counter(nums).items():
        heapq.heappush(res, (-freq, num))
    while len(ans) != k:
        ans.append(heapq.heappop(res)[1])
    return ans


# O(n)，bucket sort，参考 https://discuss.leetcode.com/topic/44237/java-o-n-solution-bucket-sort
def _solve1(nums, k):
    bucket, ans = [[] for _ in nums], []
    for num, freq in collections.Counter(nums).items():
        bucket[-freq].append(num)
    # 以下几行可以简化为 return list(itertools.chain(*bucket))[:k]
    for num_list in bucket:
        ans += num_list
        if len(ans) == k:
            return ans
