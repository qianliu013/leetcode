# coding=utf-8

"""Ugly Number II.

>>> solve = _solve
>>> solve(31)
81
"""


def _solve(n):
    res = [1] + [0] * (n - 1)
    i2 = i3 = i5 = 0
    for i in xrange(1, n):
        res[i] = min(res[i2] * 2, res[i3] * 3, res[i5] * 5)
        i2 += res[i2] * 2 == res[i]
        i3 += res[i3] * 3 == res[i]
        i5 += res[i5] * 5 == res[i]
    return res[-1]


# 来自 Runtime Distribution solution，思想是 next2 是 2 * 所有结果中的项，next3 是 3 * 只含 3 和 5 因子结果的项，next5 是只含 5 因子的项
# 此题，最快的代码是来自缓存结果的代码（貌似 leetcode 此题验证只生成一次类实例，此后直接调用函数，因此只要把结果存到类中即可）
# 下面的代码是除此外最快的，最快只需要 42 ms
def _solve1(n):
    cache, cache35 = [1] + [0] * (n - 1), [1]
    i2 = i3 = 0
    nxt_2, nxt_3, nxt_5 = 2, 3, 5
    for i in xrange(1, n):
        if nxt_2 < nxt_3 and nxt_2 < nxt_5:
            cache[i] = nxt_2
            i2 += 1
            nxt_2 = 2 * cache[i2]
        elif nxt_3 < nxt_2 and nxt_3 < nxt_5:
            cache[i] = nxt_3
            cache35.append(nxt_3)
            i3 += 1
            nxt_3 = 3 * cache35[i3]
        else:
            cache[i] = nxt_5
            cache35.append(nxt_5)
            nxt_5 *= 5
    return cache[-1]
