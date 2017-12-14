# coding=utf-8

"""Task Scheduler.

>>> solve = _solve
>>> solve(["A", "A", "A", "B", "B", "B"], 2)
8
"""

import collections


# 知道可以使用贪心策略就很容易的可以写出答案
# 寻找集合中的最大值可以使用优先队列来写，可参考 https://discuss.leetcode.com/topic/92873/c-java-clean-code-priority-queue
# 我下面的方法使用了额外的处理来保证同一 task 的时间间隔，略有些复杂；其实如果在 while 循环中，使用 0..n 循环的方式会使代码更简洁
def _solve(tasks, n):
    counter = collections.Counter(tasks)
    cold_downs = collections.defaultdict(int)
    res = 0
    while True:
        max_count = (None, 0)
        for task in cold_downs:
            cold_downs[task] -= 1
        for task, num in counter.items():
            if num > max_count[1] and cold_downs[task] <= 0:
                max_count = task, num
        if max_count[1] == 0:
            break
        else:
            cold_downs[max_count[0]] = n + 1
            counter[max_count[0]] -= 1
            res += 1
    return res + max(((num - 1) * (n + 1) + cold_downs[task] + 1 for task, num in counter.items()))


# 参考自 solution 的第一种解法 https://leetcode.com/articles/task-scheduler/
def _solve1(tasks, n):
    counts = collections.Counter(tasks).values()
    counts.sort(reverse=True)
    res, length = 0, len(counts)
    while counts[0] > 0:
        for i in xrange(n + 1):
            if counts[0] == 0:
                break
            if i < length and counts[i] > 0:
                counts[i] -= 1
            res += 1
        counts.sort(reverse=True)
    return res


# 参考自 discuss 中的高票
# 并不难理解，如果有疑惑可以去查阅 discuss 中的内容
def _solve2(tasks, n):
    counts = collections.Counter(tasks).values()
    max_count = max(counts)
    max_count_frequency = counts.count(max_count)
    return max(len(tasks), max_count_frequency + (max_count - 1) * (n + 1))
