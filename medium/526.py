# coding=utf-8

"""Beautiful Arrangement.

>>> trick = [0, 1, 2, 3, 8, 10, 36, 41, 132, 250, 700, 750, 4010, 4237, 10680, 24679]
>>> [_solve(i) for i in range(1, 16)] == trick
True
"""


# 暴力就可以过
# 从 可能性小的情况到多的情况会显著提升速度，这就是为什么从 N - 1 开始而不是 0 开始
def _solve(N):
    for i in range(1, N + 1):
        data = [[x for x in range(1, i + 1) if x % num == 0 or num % x == 0]
                for num in range(1, i + 1)]

    result = [False] * 15
    ans = [0]

    def _deep(i):
        if i == 0:
            ans[0] += 1
        else:
            for j in data[i]:
                index = j - 1
                if not result[index]:
                    result[index] = True
                    _deep(i - 1)
                    result[index] = False
    _deep(N - 1)
    return ans[0]


# 来自： https://discuss.leetcode.com/topic/79968/easy-python-230ms
# 简单的写法
def _solve1(N):
    def _count(i, unused):
        if i == 1:
            return 1
        return sum(_count(i - 1, unused - {x})
                   for x in unused
                   if x % i == 0 or i % x == 0)
    return _count(N, set(range(1, N + 1)))


print _solve(15)
