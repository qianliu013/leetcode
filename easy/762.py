# coding=utf-8
"""Prime Number of Set Bits in Binary Representation.

>>> solve = _solve
>>> solve1(6, 10)
4
>>> solve1(10, 15)
5
"""


def _solve(L, R):
    primes = {2, 3, 5, 7, 11, 13, 17, 19}
    return sum(sum((i >> j) & 1 for j in xrange(20)) in primes for i in xrange(L, R + 1))


# 此题存在 O(log(R)) 的做法：即按位考虑排列组合即可
# 代码来自：https://discuss.leetcode.com/topic/117146/o-log-r-solution-c-python-ruby
def _solve1(L, R):
    primes = {2, 3, 5, 7, 11, 13, 17, 19}

    def under(m):
        count = 0
        K = 0
        for n in xrange(19, -1, -1):
            if m & (1 << n):
                nCk = 1
                for k in xrange(n + 1):
                    if k + K in primes:
                        count += nCk
                    nCk = nCk * (n - k) / (k + 1)
                K += 1
        return count

    return under(R + 1) - under(L)
