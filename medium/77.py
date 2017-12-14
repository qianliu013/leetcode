# coding=utf-8

"""Combinations.

>>> solve = _solve2
>>> solve(4, 2)
[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
"""


from itertools import combinations


# dfs1
def _solve(n, k):
    res, cur = [], []

    # 注意，需要稍微优化一下，否则会 TLE
    def _dfs(start):
        if n - start >= k - len(cur):
            if len(cur) == k:
                res.append(list(cur))
            else:
                for i in xrange(start + 1, n + 1):
                    cur.append(i)
                    _dfs(i)
                    cur.pop()
    _dfs(0)
    return res


# dfs2
def _solve1(n, k):
    def _dfs(end, remaining):
        if remaining == 1:
            return [[i] for i in range(1, end + 1)]
        elif remaining == end:
            return [range(1, end + 1)]
        else:
            res = _dfs(end - 1, remaining)
            part = _dfs(end - 1, remaining - 1)
            for a_list in part:
                a_list.append(end)
            res += part
            return res
    return _dfs(n, k)


# Iterative，其思路是初始数组是 1~k，然后增加最后一位直到大于 n，然后倒数第二位加 1，以此类推
# 代码参考自：https://discuss.leetcode.com/topic/25958/ac-python-backtracking-iterative-solution-60-ms
# 这种想法的另一种非常 nice 的写法可参考：https://discuss.leetcode.com/topic/26689/short-iterative-c-answer-8ms
def _solve2(n, k):
    ans, cur, last = [], [], 1
    while True:
        length = len(cur)
        if length == k:
            ans.append(list(cur))
        if length == k or n - last < k - length - 1:
            if not cur:
                return ans
            last = cur.pop() + 1
        else:
            cur.append(last)
            last += 1


# python lib
def _solve3(n, k):
    return list(combinations(range(1, n + 1), k))
