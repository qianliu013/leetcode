# coding=utf-8

"""Super Ugly Number.

>>> solve = _solve
>>> solve(1331, [2, 3, 5])
360000000
"""

import heapq


def _solve(n, primes):
    res = [1]
    heap = [(prime, 0, prime) for prime in primes]
    heapq.heapify(heap)
    while len(res) < n:
        cur, index, prime = heapq.heappop(heap)
        if cur != res[-1]:
            res.append(cur)
        heapq.heappush(heap, (prime * res[index], index + 1, prime))
    return res[-1]


# 实际上，上述代码虽然经过堆优化，但由于数据特点（K 较小），实际速度并没有下面较为暴力的代码快
def _solve1(n, primes):
    res, length = [], len(primes)
    i_list, nxt_list = [0] * length, [1] * length
    for _ in xrange(n):
        cur = min(nxt_list)
        res.append(cur)
        for i in xrange(length):
            if cur == nxt_list[i]:
                nxt_list[i] = res[i_list[i]] * primes[i]
                i_list[i] += 1
    return res[-1]
